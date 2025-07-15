# 🛠️ MySQL Data Recovery Tool

This is a simple Python script to **recover MySQL table data files** (`.frm`, `.ibd`, etc.) from a backup folder and copy them into your active MySQL data directory. It's useful when recovering crashed MySQL databases using XAMPP, WAMP, or standalone MySQL installations.

---

## 📦 Features

- Recursively copies MySQL table files (`.frm`, `.ibd`, `.myd`, `.myi`, etc.)
- Preserves folder structure (per-database)
- CLI-based and easy to configure
- Helpful for restoring backups or recovering from `ibdata1`/InnoDB issues

---

## ⚙️ Requirements

- Python 3.x
- Access to your MySQL/XAMPP data directories
- Optional: `innodb_force_recovery` in `my.ini` for InnoDB crashes

---

## 🚀 How to Use

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/mysql-data-recovery.git
   cd mysql-data-recovery
   Run the script:
   python recover_mysql_data.py
