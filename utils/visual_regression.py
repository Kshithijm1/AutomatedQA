import logging
from PIL import ImageChops, Image
import os

def run_visual_regression_tests():
    baseline_dir = 'baseline_images'
    current_dir = 'current_images'

    # Check if baseline directory exists; if not, create it
    if not os.path.exists(baseline_dir):
        logging.warning(f"{baseline_dir} does not exist. Creating directory.")
        os.makedirs(baseline_dir)

    # Check if current directory exists; if not, create it
    if not os.path.exists(current_dir):
        logging.warning(f"{current_dir} does not exist. Creating directory.")
        os.makedirs(current_dir)

    # Get list of images in baseline directory
    baseline_images = os.listdir(baseline_dir)
    if not baseline_images:
        logging.info("No images found for comparison. Skipping visual regression tests.")
        return

    # Iterate through each image in the baseline directory
    for filename in baseline_images:
        baseline_image_path = os.path.join(baseline_dir, filename)
        current_image_path = os.path.join(current_dir, filename)

        # Check if corresponding image exists in the current directory
        if os.path.exists(current_image_path):
            logging.info(f"Comparing {baseline_image_path} with {current_image_path}")
            baseline_image = Image.open(baseline_image_path)
            current_image = Image.open(current_image_path)
            diff = ImageChops.difference(baseline_image, current_image)
            
            # Save the diff image if differences are found
            if diff.getbbox():
                diff_path = os.path.join('diff_images', filename)
                diff.save(diff_path)
                logging.info(f"Visual differences found in {filename}, saved diff image.")
            else:
                logging.info(f"No differences found in {filename}.")
        else:
            logging.warning(f"{current_image_path} does not exist for comparison.")

    logging.info("Visual regression tests completed.")

    # Generate a report of the screenshot comparisons
    def generate_screenshot_comparison_report():
        logging.info("Generating screenshot comparison report...")
        report_content = "Screenshot comparison report:\n"
        for filename in baseline_images:
            report_content += f"- Compared {filename}\n"
        logging.info(report_content)

    generate_screenshot_comparison_report()

    # Detect changes in specific regions of images
    def detect_changes_in_regions():
        logging.info("Detecting changes in specific regions of images...")
        region_changes = []
        for filename in baseline_images:
            baseline_image = Image.open(os.path.join(baseline_dir, filename))
            current_image = Image.open(os.path.join(current_dir, filename))
            region = (50, 50, 200, 200)  # Example region
            baseline_region = baseline_image.crop(region)
            current_region = current_image.crop(region)
            if ImageChops.difference(baseline_region, current_region).getbbox():
                region_changes.append(filename)
        if region_changes:
            logging.warning(f"Changes detected in regions for images: {region_changes}")
        else:
            logging.info("No changes detected in specified regions.")

    detect_changes_in_regions()
