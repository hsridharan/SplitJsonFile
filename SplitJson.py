import json
import os
import argparse

def extract_content_from_json(input_file_path, key_to_extract, output_file_suffix="_extracted"):
    try:
        # Ensure the input file is a JSON file
        if not input_file_path.endswith(".json"):
            raise ValueError("Input file must be a JSON file.")

        # Read the JSON file
        print(f"Reading JSON file from: {input_file_path}")
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            data = json.load(input_file)

        # Extract the specific content
        print(f"Extracting content for key: {key_to_extract}")
        extracted_content = data.get(key_to_extract, {})

        # Add the new elements
        for item in extracted_content:
            item["ItemClass"] = "TenantSkillTest"
            item["skillId@Is.Queryable"] = ""
            item["skillId@odata.type"] = "String"
            item["Name@Is.Queryable"] = "true"
            item["Name@odata.type"] = "String"
            item["Description@Is.Queryable"] = "true"
            item["Description@odata.type"] = "String"
            item["roles@odata.type"] = "Collection(String)"
            item["SecondaryKey"] = "urn:tenant:skill:exCode1"
            item["Name"] = item.get("translations", {}).get("en_US", {}).get("Name", "")
            item["Description"] = item.get("translations", {}).get("en_US", {}).get("Description", "")

        # Create the output file path
        base_name = os.path.basename(input_file_path)
        directory_name = os.path.dirname(input_file_path)
        output_file_name = f"{os.path.splitext(base_name)[0]}{output_file_suffix}.json"
        output_file_path = os.path.join(directory_name, output_file_name)

        # Save the extracted content to a new JSON file
        print(f"Saving extracted content to: {output_file_path}")
        with open(output_file_path, 'w') as output_file:
            json.dump(extracted_content, output_file, indent=4)

        print(f"Extracted content saved successfully to: {output_file_path}")

    except FileNotFoundError:
        print(f"Error: The file {input_file_path} does not exist.")
    except json.JSONDecodeError as e:
        print(f"Error: The file {input_file_path} is not a valid JSON file. {e}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Extract content from a JSON file.")
    parser.add_argument("input_file_path", type=str, help="Path to the input JSON file.")
    parser.add_argument("key_to_extract", type=str, help="Key to extract from the JSON file.")
    args = parser.parse_args()

    extract_content_from_json(args.input_file_path, args.key_to_extract)
    # input_file_path = 'C:/VivaSkills/TenantScript/tenant.json'
    # extract_content_from_json(input_file_path, "TenantCustomSkills")

if __name__ == "__main__":
    main()
