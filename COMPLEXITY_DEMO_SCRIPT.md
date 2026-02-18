# Cyclomatic Complexity Demo - Instructional Script

## 🎯 Learning Objective
Teach students about **Cyclomatic Complexity** as a code quality metric and how CI pipelines can enforce quality gates to prevent unmaintainable code from entering the codebase.

---

## 📚 Whats Cyclomatic Complexity?

**Definition**: A software metric that measures the number of independent paths through a program's source code.

**Simple Formula**: 
```
Cyclomatic Complexity = Number of decision points + 1
```

**Decision points include**:
- `if` statements
- `else` statements
- `for` loops
- `while` loops
- `case` statements
- Boolean operators (`&&`, `||`)

**Industry Standards**:
- **1-5**: Simple, low risk, easy to test
- **6-10**: Moderate complexity, acceptable
- **11-20**: Complex, high risk, hard to maintain
- **21+**: Very high risk, UNMAINTAINABLE

---

## 🎬 Demo Script

### Step 1: Introduce the "Bad" Code

**What to Say**:
> "I've written a student grade calculator. It works, but let's see what happens when we push it to our repository with quality gates enabled."

**Show the Code**:
Open `messy_logic.py` and scroll through the nested if/else statements.

**Key Points**:
- Point out the **15+ levels of nesting**
- Mention how hard it would be to:
  - Add a new grading criterion
  - Find and fix a bug
  - Write comprehensive tests
  - Understand what the code does

**What to Say**:
> "This function has ONE job - calculate a grade. But look at this mess! How many possible paths are there through this code? Dozens! This is a maintenance nightmare."

---

### Step 2: Push and Watch the Pipeline Fail

**Actions**:
```bash
git add messy_logic.py .github/workflows/quality_gate.yml
git commit -m "Add student grade calculator with quality gate"
git push origin main
```

**What to Show**:
1. Navigate to GitHub → **Actions** tab
2. Click on the running workflow: **"Code Quality Gate - Cyclomatic Complexity Check"**
3. Watch it fail with a **red X** ❌

**What to Say**:
> "The pipeline is running our quality checks automatically. Let's see what happens..."

---

### Step 3: Explain the Failure

**Click into the failed job** and show the **"Check Cyclomatic Complexity"** step.

**Expected Error Output**:
```
messy_logic.py:13:1: C901 'calculate_student_grade' is too complex (XX)
```

Where `XX` is the actual complexity score (likely 20-30+).

**What to Say**:
> "Our quality gate is configured with `--max-complexity=5`. This means any function with a cyclomatic complexity greater than 5 will fail the build."

**Explain the Error**:
- **C901**: Flake8 error code for "function is too complex"
- **Line 13**: Where the function starts
- **Complexity score**: The actual measured complexity

**Key Teaching Points**:
- ✅ **Automated Quality Gates**: The pipeline prevents bad code from being accepted
- ✅ **Objective Metrics**: Not subjective - it's a measurable number
- ✅ **Early Detection**: Caught before code review, before merge, before production
- ✅ **Team Standards**: Enforces consistent quality across all developers

---

### Step 4: Show the Solution (Refactoring)

**What to Say**:
> "So how do we fix this? We need to refactor this function to reduce complexity. Here are some strategies:"

**Refactoring Strategies**:

1. **Extract Methods** - Break into smaller functions
2. **Use Data Structures** - Replace nested ifs with lookup tables
3. **Early Returns** - Reduce nesting depth
4. **Strategy Pattern** - Use polymorphism instead of conditionals

**Example Refactored Code** (show on screen):

```python
def calculate_student_grade(score, attendance, assignments_completed, 
                           participation, extra_credit, late_submissions,
                           group_project_score, midterm_score, 
                           final_exam_score, is_honors_student):
    """
    Calculate final grade - REFACTORED VERSION
    Cyclomatic Complexity: ~5 (ACCEPTABLE)
    """
    
    # Use a scoring system instead of nested ifs
    total_points = calculate_total_points(
        score, attendance, assignments_completed, 
        participation, extra_credit, late_submissions,
        group_project_score, midterm_score, final_exam_score
    )
    
    # Apply honors bonus
    if is_honors_student and total_points >= 90:
        total_points += 2
    
    # Simple lookup instead of nested conditionals
    return get_letter_grade(total_points)


def calculate_total_points(score, attendance, assignments_completed,
                          participation, extra_credit, late_submissions,
                          group_project_score, midterm_score, final_exam_score):
    """Calculate weighted total - Complexity: 1"""
    points = (score * 0.4 + 
              attendance * 0.1 + 
              (assignments_completed / 20) * 100 * 0.15 +
              participation * 0.1 +
              group_project_score * 0.1 +
              midterm_score * 0.075 +
              final_exam_score * 0.075)
    
    points += extra_credit
    points -= (late_submissions * 2)  # Penalty for late work
    
    return points


def get_letter_grade(points):
    """Convert points to letter grade - Complexity: 1"""
    grade_thresholds = [
        (97, "A+"), (93, "A"), (90, "A-"),
        (87, "B+"), (83, "B"), (80, "B-"),
        (77, "C+"), (73, "C"), (70, "C-"),
        (67, "D+"), (63, "D"), (60, "D-"),
        (0, "F")
    ]
    
    for threshold, grade in grade_thresholds:
        if points >= threshold:
            return grade
    
    return "F"
```

**What to Say**:
> "Now we've broken one complex function into three simple functions. Each has a single responsibility and low complexity. This is much easier to test, maintain, and understand."

---

### Step 5: Push the Fixed Code (Optional)

If you want to show the green checkmark:

```bash
git add messy_logic.py
git commit -m "Refactor: Reduce cyclomatic complexity using helper functions"
git push origin main
```

**Show**: Green checkmark ✅ in GitHub Actions

---

## 🎓 Discussion Questions for Students

1. **Why is high complexity bad?**
   - Harder to test (more paths = more test cases)
   - More bugs hide in complex code
   - Difficult for new team members to understand
   - Expensive to maintain and modify

2. **When should we measure complexity?**
   - During code review
   - In CI/CD pipelines (automated)
   - Before merging to main branch

3. **What's an acceptable complexity threshold?**
   - Depends on the team/project
   - Common thresholds: 5-10
   - Critical code (security, payments): Lower threshold (3-5)
   - Less critical code: Higher threshold (10-15)

4. **What other quality metrics exist?**
   - Code coverage (% of code tested)
   - Code duplication
   - Lines of code per function
   - Maintainability index

---

## 📊 Real-World Impact

**Case Study - NASA**:
- NASA requires cyclomatic complexity < 10 for flight software
- Critical safety systems must be < 5
- Reason: Lives depend on code correctness

**Case Study - Google**:
- Enforces complexity limits in code review tools
- Automated checks prevent merging complex code
- Result: More maintainable codebase at scale

---

## 🔧 Tools for Measuring Complexity

**Python**:
- `flake8` with `mccabe` plugin (used in this demo)
- `radon` - Detailed complexity metrics
- `pylint` - Includes complexity checks

**JavaScript**:
- `eslint` with `complexity` rule
- `plato` - Complexity visualization

**Java**:
- `checkstyle`
- `PMD`
- SonarQube

**Multi-language**:
- SonarQube (enterprise)
- CodeClimate
- Codacy

---

## ✅ Key Takeaways

1. **Cyclomatic Complexity** measures code complexity objectively
2. **Quality Gates** in CI/CD prevent bad code from entering the codebase
3. **Refactoring** reduces complexity and improves maintainability
4. **Automation** enforces standards consistently across the team
5. **Simple code** is easier to test, debug, and maintain

---

## 📝 Assignment Ideas

1. **Measure Complexity**: Have students analyze their own code with flake8
2. **Refactoring Challenge**: Give them complex code to refactor
3. **Set Up Quality Gates**: Add complexity checks to their projects
4. **Compare Metrics**: Measure before/after refactoring
