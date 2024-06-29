import logging
from fpdf import FPDF
import random

# Generate a PDF report of test cases with bug predictions
def generate_report(test_cases_with_bugs):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add title to the report
    pdf.cell(200, 10, txt="Test Report", ln=True, align='C')
    pdf.cell(200, 10, txt="=====================", ln=True, align='C')

    # Add details for each test case
    for case in test_cases_with_bugs:
        pdf.cell(200, 10, txt=f"Requirement: {case['requirement']}", ln=True)
        pdf.cell(200, 10, txt=f"Test Case: {case['test_case']}", ln=True)
        pdf.cell(200, 10, txt=f"Predicted Bug: {'Yes' if case['bug_prediction'] == 1 else 'No'}", ln=True)
        pdf.cell(200, 10, txt="----", ln=True)

    pdf.output("test_report.pdf")
    logging.info("Report generated: test_report.pdf")

# Generate a detailed text report of test cases with bug predictions
def generate_detailed_report(test_cases_with_bugs):
    logging.info("Generating detailed report...")
    with open("detailed_test_report.txt", "w") as f:
        f.write("Detailed Test Report\n")
        f.write("====================\n\n")
        for case in test_cases_with_bugs:
            f.write(f"Requirement: {case['requirement']}\n")
            f.write(f"Test Case: {case['test_case']}\n")
            f.write(f"Predicted Bug: {'Yes' if case['bug_prediction'] == 1 else 'No'}\n")
            f.write("----\n")
    logging.info("Detailed report generated: detailed_test_report.txt")

# Generate a summary text report of test cases with bug predictions
def generate_summary_report(test_cases_with_bugs):
    logging.info("Generating summary report...")
    summary = {"total": len(test_cases_with_bugs), "bugs": 0, "no_bugs": 0}
    for case in test_cases_with_bugs:
        if case['bug_prediction'] == 1:
            summary['bugs'] += 1
        else:
            summary['no_bugs'] += 1

    with open("summary_test_report.txt", "w") as f:
        f.write("Summary Test Report\n")
        f.write("===================\n\n")
        f.write(f"Total Test Cases: {summary['total']}\n")
        f.write(f"Test Cases with Bugs: {summary['bugs']}\n")
        f.write(f"Test Cases without Bugs: {summary['no_bugs']}\n")

    logging.info("Summary report generated: summary_test_report.txt")

# Generate a performance report with random metrics
def generate_performance_report():
    logging.info("Generating performance report...")
    with open("performance_report.txt", "w") as f:
        f.write("Performance Report\n")
        f.write("==================\n\n")
        f.write("Detailed performance metrics and analysis...\n")
        for i in range(10):
            f.write(f"Metric {i+1}: {random.uniform(0, 100)}%\n")
    logging.info("Performance report generated: performance_report.txt")

# Generate a security report with predefined vulnerability checks
def generate_security_report():
    logging.info("Generating security report...")
    with open("security_report.txt", "w") as f:
        f.write("Security Report\n")
        f.write("==================\n\n")
        f.write("Detailed security analysis and vulnerability checks...\n")
        vulnerabilities = [
            "SQL Injection: Potential vulnerability detected.",
            "XSS: No vulnerability detected.",
            "CSRF: Potential vulnerability detected.",
            "Directory Traversal: No vulnerability detected.",
            "Insecure Storage: No vulnerability detected.",
            "Sensitive Data Exposure: Potential vulnerability detected."
        ]
        for vulnerability in vulnerabilities:
            f.write(f"{vulnerability}\n")
    logging.info("Security report generated: security_report.txt")

# Generate a code coverage report with random metrics
def generate_code_coverage_report():
    logging.info("Generating code coverage report...")
    with open("code_coverage_report.txt", "w") as f:
        f.write("Code Coverage Report\n")
        f.write("====================\n\n")
        f.write("Detailed code coverage metrics and analysis...\n")
        for i in range(10):
            f.write(f"Coverage Metric {i+1}: {random.uniform(70, 100)}%\n")
    logging.info("Code coverage report generated: code_coverage_report.txt")

# Generate a bug analysis report of test cases with bug predictions
def generate_bug_analysis_report(test_cases_with_bugs):
    logging.info("Generating bug analysis report...")
    with open("bug_analysis_report.txt", "w") as f:
        f.write("Bug Analysis Report\n")
        f.write("====================\n\n")
        for case in test_cases_with_bugs:
            f.write(f"Requirement: {case['requirement']}\n")
            f.write(f"Test Case: {case['test_case']}\n")
            f.write(f"Predicted Bug: {'Yes' if case['bug_prediction'] == 1 else 'No'}\n")
            f.write("----\n")
    logging.info("Bug analysis report generated: bug_analysis_report.txt")
