import csv
import datetime
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QMessageBox,
    QSpacerItem,
    QSizePolicy
)
from PyQt5.QtGui import QFont

class UrenregistratieApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Urenregistratiesysteem")
        self.setFixedSize(600, 550)  # Set fixed window size (600 width, 550 height)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Apply dark theme and change font
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: white;
                font-family: Arial, sans-serif;
            }
            QLabel {
                font-size: 24px; /* Larger font size */
                padding-bottom: 15px; /* Increased padding */
            }
            QLineEdit, QPushButton {
                font-size: 22px; /* Larger font size */
                padding: 10px; /* Increased padding */
                background-color: #2e2e2e;
                border: 1px solid #3a3a3a;
                color: white;
            }
            QPushButton {
                transition: all 0.3s ease; /* Smooth transition */
            }
            QPushButton:hover {
                background-color: #3e3e3e;
                transform: scale(0.95); /* Scale down on hover */
            }
            QPushButton:pressed {
                background-color: #1e1e1e;
            }
        """)

        self.naam_label = QLabel("Naam:")
        layout.addWidget(self.naam_label)
        self.naam_label.setFont(QFont("Arial", 24))  # Set font size for label
        self.naam_input = QLineEdit()
        layout.addWidget(self.naam_input)

        self.datum_label = QLabel("Datum (DD-MM-YYYY):")  # Change the label text
        layout.addWidget(self.datum_label)
        self.datum_label.setFont(QFont("Arial", 24))  # Set font size for label
        self.datum_input = QLineEdit()
        layout.addWidget(self.datum_input)

        self.uren_label = QLabel("Uren:")
        layout.addWidget(self.uren_label)
        self.uren_label.setFont(QFont("Arial", 24))  # Set font size for label
        self.uren_input = QLineEdit()
        layout.addWidget(self.uren_input)

        self.project_label = QLabel("Project:")
        layout.addWidget(self.project_label)
        self.project_label.setFont(QFont("Arial", 24))  # Set font size for label
        self.project_input = QLineEdit()
        layout.addWidget(self.project_input)

        # Add spacer item for vertical spacing
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer_item)

        self.submit_button = QPushButton("Opslaan")
        self.submit_button.clicked.connect(self.submit_form)
        layout.addWidget(self.submit_button)
        self.submit_button.setFont(QFont("Arial", 24))  # Set font size for button

        self.setLayout(layout)

    def submit_form(self):
        naam = self.naam_input.text()
        datum = self.datum_input.text()
        uren = self.uren_input.text()
        project = self.project_input.text()

        try:
            # Adjust date format from "DD-MM-YYYY" to "YYYY-MM-DD" for datetime parsing
            datetime.datetime.strptime(datum, "%d-%m-%Y")
            uren = float(uren)
            if uren < 0:
                raise ValueError("Negatieve uren zijn niet toegestaan.")
        except ValueError as e:
            self.show_error_message("Ongeldige invoer. Probeer opnieuw.")
            return

        # Format date as "YYYY-MM-DD" for CSV storage
        formatted_date = datetime.datetime.strptime(datum, "%d-%m-%Y").strftime("%Y-%m-%d")

        data.append({'Naam': naam, 'Datum': formatted_date, 'Uren': uren, 'Project': project})
        save_to_csv(data)
        self.show_success_message("Gegevens zijn opgeslagen in 'urenregistratie.csv'.")

    def show_error_message(self, message):
        QMessageBox.critical(self, "Fout", message)

    def show_success_message(self, message):
        QMessageBox.information(self, "Succes", message)

def save_to_csv(data):
    headers = ['Naam', 'Datum', 'Uren', 'Project']
    with open('urenregistratie.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()  # Write header row
        writer.writerows(data)

if __name__ == "__main__":
    data = []
    app = QApplication([])
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
    window = UrenregistratieApp()
    window.show()
    app.exec_()
