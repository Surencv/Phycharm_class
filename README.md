Requisition Management System & Academic Performance Evaluator

 Overview
This repository contains two Python-based modules:

1. Requisition Management System– Automates staff requisition tracking, approval logic, and statistical reporting.
2. Academic Performance Evaluator– Calculates total and average marks, assigns grades, and determines pass/fail status.

Each module demonstrates foundational software design principles through structured logic, modular functions, and clear output formatting.
Design Principles Demonstrated

1.Modularity
Code is broken into reusable components:
  - `Requisition` class encapsulates requisition logic.
  - `respond()` and `display()` methods isolate decision and output behavior.
  - `calculate_average()` and `assign_grade()` functions separate concerns in the academic module.

2.Encapsulation
- Requisition attributes (e.g., `staff_id`, `items`, `status`) are bundled within the class.
- Internal logic like approval reference generation is hidden from external access.

3.Single Responsibility Principle
- Each function and method performs one clear task:
  - `respond()` updates status.
  - `show_statistics()` summarizes requisition data.
  - `main()` orchestrates input/output without mixing logic.
    
 4.Scalability
- Global counters and lists allow easy extension to persistent storage or database integration.
- Subject lists and keyword arguments (`**scores`) support flexible input handling.

5.Readability & Maintainability
- Inline comments clarify each step.
- Variable names are descriptive (`total_marks`, `average_marks`, `approval_ref`).
- Output is consistently formatted for user clarity.


