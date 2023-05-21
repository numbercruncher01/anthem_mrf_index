import sqlite3
import ijson

# Connect to SQLite database
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Create table
c.execute('''
    CREATE TABLE IF NOT EXISTS anthem_index(
        reporting_entity_name TEXT,
        reporting_entity_type TEXT,
        plan_name TEXT,
        plan_id_type TEXT,
        plan_id TEXT,
        plan_market_type TEXT,
        description TEXT,
        location TEXT
    )
''')

# Commit the changes
conn.commit()

# Parse JSON file
with open('A:\\Anthem\\2023-05-01_anthem_index.json', 'r') as f:
    data = ijson.items(f, '')

    # Get the first item of the json file which is a dict
    first_dict = next(data)

    # Extract required fields
    reporting_entity_name = first_dict['reporting_entity_name']
    reporting_entity_type = first_dict['reporting_entity_type']

    # Start a transaction
    c.execute('BEGIN TRANSACTION')

    try:
        # Traverse reporting_structure
        for struct in first_dict['reporting_structure']:
            for reporting_plan in struct['reporting_plans']:
                for in_network_file in struct.get('in_network_files', []):
                    c.execute('''
                        INSERT INTO anthem_index VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        reporting_entity_name,
                        reporting_entity_type,
                        reporting_plan['plan_name'],
                        reporting_plan['plan_id_type'],
                        reporting_plan['plan_id'],
                        reporting_plan['plan_market_type'],
                        in_network_file['description'],
                        in_network_file['location']
                    ))

            if 'allowed_amount_file' in struct:
                for reporting_plan in struct['reporting_plans']:
                    c.execute('''
                        INSERT INTO anthem_index VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        reporting_entity_name,
                        reporting_entity_type,
                        reporting_plan['plan_name'],
                        reporting_plan['plan_id_type'],
                        reporting_plan['plan_id'],
                        reporting_plan['plan_market_type'],
                        struct['allowed_amount_file']['description'],
                        struct['allowed_amount_file']['location']
                    ))

        # Commit the transaction
        c.execute('COMMIT')

    except Exception as e:
        # There was an error, rollback the transaction
        conn.rollback()
        print(f"An error occurred: {e}")

# Close the connection
conn.close()
