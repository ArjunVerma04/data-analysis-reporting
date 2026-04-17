import pandas as pd
import matplotlib.pyplot as plt
from database import create_database, get_connection

create_database()
conn = get_connection()

df = pd.read_sql("SELECT * FROM business", conn)

# Total Revenue
print("Total Revenue:", df["Revenue"].sum())

# Monthly Report
monthly = df.groupby("Region")["Revenue"].sum()
print(monthly)

# Chart
monthly.plot(kind="bar", title="Revenue by Region")
plt.tight_layout()
plt.savefig("reports/revenue_by_region.png")
plt.show()