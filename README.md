# anthem_mrf_index
Code to Parse Anthem's MRF Index
👨‍💻Calling all data engineers…   Can you beat my runtime???  I'll post the winner and their code on www.brightspotinsights.com

⌛Using the attached python code, I was able to parse the Anthem MRF JSON (19.5GBs) into a SQLite database with a runtime of 9mins.  

The final size of the SQLite database is 110.6GB.

I'd love to be able to run it faster, but this is as far as I could optimize it.  Other versions of the code had a runtime of 13 mins, so I was able to make some improvements.  However, I'd love to know if you can run it faster.  Feel free to modify the code or use other languages.

💻I'm running the code on a PC with i9-32 core (13Gen), 128GB Ram (DDR5), and NVMe Gen 4 SSD 

Key Steps:
	1. Download the Compressed MRF Index from Anthem (9.3GB) Link: https://antm-pt-prod-dataz-nogbd-nophi-us-east1.s3.amazonaws.com/anthem/2023-05-01_anthem_index.json.gz
	2. Unzip file and store JSON locally.  File expands to  19.6GB
	3. Update Python code to point to the location of your Anthem JSON File
	4. Modify and optimize code
	5. Run Code
  	6. Capture screenshot of your SQLite database "Date created",  "Date modified", & "Size"
   
   Post screenshot here![image](https://github.com/numbercruncher01/anthem_mrf_index/assets/77574184/9af2fbea-5f79-45ca-a262-53e50db2f84f)
