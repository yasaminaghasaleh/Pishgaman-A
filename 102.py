info = [
    {"Name": "Yasamin", "Age": 15, "Job": "Front-End Dev"},
    {"Name": "Shayan", "Age": 15, "Job": "Front-End Dev"},
    {"Name": "Ilia", "Age": 15, "Job": "Back-End Dev"},
    {"Name": "Sajad", "Age": 18, "Job": "DB Man"},
    {"Name": "Benyamin", "Age": 15, "Job": "Security Engineer"},
    {"Name": "Arash", "Age": 21, "Job": "Back-End Dev", }
]

html = """
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
  border-radius: 10px;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #cf514d;
  color: white;
}
</style>
</head>
<body>

<h1>Employees : </h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Age</th>
    <th>Job Title</th>
  </tr>
  
"""
for person in info :
    html += f"""
      <tr>
        <td>{person["Name"]}</td>
        <td>{person["Age"]}</td>
        <td>{person["Job"]}</td>
      </tr>
    """

html += """
</table>
</body>
</html>
"""

open("Info.html","w").write(html)
print("Done")
