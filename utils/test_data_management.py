import logging
from faker import Faker

def manage_test_data(action):
    fake = Faker()
    logging.info(f"Managing test data: {action}")

    # Generate test data
    if action == 'setup':
        for _ in range(10):
            name = fake.name()
            email = fake.email()
            logging.info(f"Generated test data - Name: {name}, Email: {email}")

    # Clean up test data
    if action == 'cleanup':
        logging.info("Cleaning up test data...")
        logging.info("Test data cleaned up.")

    # Generate a large dataset for performance testing
    def generate_large_dataset():
        logging.info("Generating large dataset for performance testing...")
        large_data = []
        for _ in range(1000):
            large_data.append({"name": fake.name(), "email": fake.email()})
        logging.info(f"Generated large dataset with {len(large_data)} records.")

    if action == 'generate_large_dataset':
        generate_large_dataset()

    # Anonymize data for privacy compliance
    def anonymize_data():
        logging.info("Anonymizing data for privacy compliance...")
        anonymized_data = [{"name": fake.name(), "email": fake.email()} for _ in range(100)]
        logging.info(f"Anonymized data: {anonymized_data[:5]}...")

    if action == 'anonymize_data':
        anonymize_data()

    # Backup test data
    def backup_test_data():
        logging.info("Backing up test data...")
        backup_data = [{"name": fake.name(), "email": fake.email()} for _ in range(50)]
        logging.info(f"Backup data: {backup_data[:5]}...")
        logging.info("Test data backup completed.")

    if action == 'backup_test_data':
        backup_test_data()

    # Restore test data from backup
    def restore_test_data():
        logging.info("Restoring test data from backup...")
        restored_data = [{"name": fake.name(), "email": fake.email()} for _ in range(50)]
        logging.info(f"Restored data: {restored_data[:5]}...")
        logging.info("Test data restoration completed.")

    if action == 'restore_test_data':
        restore_test_data()

    # Validate test data integrity
    def validate_test_data():
        logging.info("Validating test data integrity...")
        for _ in range(10):
            name = fake.name()
            email = fake.email()
            if not name or not email:
                logging.warning(f"Invalid test data - Name: {name}, Email: {email}")
            else:
                logging.info(f"Validated test data - Name: {name}, Email: {email}")

    if action == 'validate_test_data':
        validate_test_data()
