1. Clone the file "SplitJson.py" to a folder e.g : C:\Test
2. Keep the actual file which needs extraction in the same folder. e.g : C:\Test\tenant.json
3. Run the following command in powershell: 
PS C:\Test> ./SplitJson.py "C:/Test/tenant.json" "TenantCustomSkills"
tenant.json - Name of the input JSON file
TenantCustomSkills - Node of the JSON which is extracted.
5. A New file with name e.g: "tenant_extracted.json" will be saved in the same path: 

![image](https://github.com/hsridharan/SplitJsonFile/assets/74435183/3c1ea308-dc4a-4c86-a1d6-aedbf73679d0)


