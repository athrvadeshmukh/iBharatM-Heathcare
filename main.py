import sys
import requests
from io import BytesIO
from PIL import Image, ImageQt, UnidentifiedImageError
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton,
    QFileDialog, QLineEdit, QDialog, QComboBox, QMessageBox, QSplitter, QFrame, QMenu
)
from PySide6.QtGui import QPixmap, QAction
from PySide6.QtCore import Qt
from PySide6.QtWebEngineWidgets import QWebEngineView
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch Prediction Key and Endpoint URL from environment variables
PREDICTION_KEY = os.getenv("PREDICTION_KEY")
IMAGE_PREDICTION_URL = os.getenv("IMAGE_PREDICTION_URL")
URL_PREDICTION_URL = os.getenv("URL_PREDICTION_URL")


# Azure Prediction Function
def predict_image(image_path=None, image_url=None):
    try:
        headers = {
            "Prediction-Key": PREDICTION_KEY  # Use the Prediction Key from the environment variable
        }

        if image_path:
            # Image-based prediction
            response = None
            with open(image_path, "rb") as image_file:
                response = requests.post(IMAGE_PREDICTION_URL, headers=headers, data=image_file)

        elif image_url:
            # URL-based prediction
            body = {"Url": image_url}
            response = requests.post(URL_PREDICTION_URL, headers=headers, json=body)

        if response and response.status_code == 200:
            return response.json()
        else:
            print(f"Error in prediction: {response.status_code} - {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IBharatM Chest X Ray Vision AI")
        self.setGeometry(100, 100, 1000, 600)
        self.showMaximized()
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        splitter = QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)

        # Left Panel
        left_panel = QWidget()
        splitter.addWidget(left_panel)
        left_layout = QVBoxLayout(left_panel)

        # Image Display
        self.image_frame = QFrame(self)
        self.image_frame.setFixedSize(400, 400)
        self.image_layout = QVBoxLayout(self.image_frame)
        self.image_label = QLabel("Image will be displayed here", self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_layout.addWidget(self.image_label)
        left_layout.addWidget(self.image_frame)

        # Buttons for Upload and URL
        upload_btn = QPushButton("Upload Image", self)
        upload_btn.clicked.connect(self.upload_image)
        left_layout.addWidget(upload_btn)

        url_btn = QPushButton("Enter Image URL", self)
        url_btn.clicked.connect(self.enter_image_url)
        left_layout.addWidget(url_btn)

        # Right Panel
        right_panel = QWidget()
        splitter.addWidget(right_panel)
        right_layout = QVBoxLayout(right_panel)

        # Prediction Results
        self.result_label = QLabel("Prediction results will be displayed here", self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("border: 2px solid black; padding: 10px; font-size: 16px;")
        right_layout.addWidget(self.result_label)

        # Chart Type Selection
        self.chart_combo = QComboBox(self)
        self.chart_combo.addItems(["Bar Graph", "Pie Chart", "Progress Bar"])
        self.chart_combo.currentIndexChanged.connect(self.update_graph)
        right_layout.addWidget(self.chart_combo)

        # Graph Display
        self.graph_canvas = FigureCanvas(plt.Figure())
        right_layout.addWidget(self.graph_canvas)

        self.create_menu_bar()

    def create_menu_bar(self):
        menu_bar = self.menuBar()

        # Help Menu
        help_menu = QMenu("Help", self)
        menu_bar.addMenu(help_menu)

        how_to_use_action = QAction("How to Use", self)
        how_to_use_action.triggered.connect(self.show_how_to_use)
        help_menu.addAction(how_to_use_action)

        developer_action = QAction("Developer", self)
        developer_action.triggered.connect(self.show_developer)
        help_menu.addAction(developer_action)

        # Legal Menu
        legal_menu = QMenu("Legal", self)
        menu_bar.addMenu(legal_menu)

        terms_action = QAction("Terms and Conditions", self)
        terms_action.triggered.connect(self.show_terms)
        legal_menu.addAction(terms_action)

        privacy_action = QAction("Privacy Policy", self)
        privacy_action.triggered.connect(self.show_privacy)
        legal_menu.addAction(privacy_action)

        # Ask Health Bot Menu
        ask_health_bot_menu = QMenu("Ask Health Bot", self)
        menu_bar.addMenu(ask_health_bot_menu)

        ask_health_bot_action = QAction("Open Health Bot", self)
        ask_health_bot_action.triggered.connect(self.open_health_bot)
        ask_health_bot_menu.addAction(ask_health_bot_action)

    def open_health_bot(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Ask Health Bot")
        dialog.resize(800, 600)

        layout = QVBoxLayout(dialog)
        web_view = QWebEngineView(dialog)
        web_view.setUrl("https://healthcare-bot-4zh3cgtuvfxc6.azurewebsites.net/")
        layout.addWidget(web_view)

        dialog.exec_()

    def show_how_to_use(self):
        QMessageBox.information(self, "How to Use", "1. Click on 'Upload Image' to select an image file from your computer.\n2. Click on 'Enter Image URL' to enter the URL of an image.\n3. The application will display the image and the prediction results.\n4. You can select the chart type from the dropdown to view the prediction results in different formats.")

    def show_developer(self):
        QMessageBox.information(self, "Developer", " Athrva Deshmukh, Gourav Kushwaha, Sonu Kushwaha and Naushad Ali.")

    def show_contribute(self):
        QMessageBox.information(self, "Contribute Us", "https://github.com/athrvadeshmukh/iBharatM-Heathcare")


    def show_terms(self):
        QMessageBox.information(self, "Licence", "Copyright 2024 Athrva Deshmukh, Gourav Kushwaha, Sonu Kushwaha and Naushad Ali,    Copyright 2024 Athrva Deshmukh\n\nLicensed under the Apache License, Version 2.0 (the \"License\");\nYou may not use this file except in compliance with the License.\nYou may obtain a copy of the License at\n\n    http://www.apache.org/licenses/LICENSE-2.0")


    def show_privacy(self):
        QMessageBox.information(self, "Privacy Policy", "Application privacy policy.")

    def upload_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Upload Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*)", options=options)
        if file_path:
            self.display_image(file_path)
            result = predict_image(image_path=file_path)
            if result:
                self.display_result(result)
            else:
                QMessageBox.warning(self, "Error", "Failed to get prediction results.")

    def enter_image_url(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Enter Image URL")
        layout = QVBoxLayout(dialog)

        url_input = QLineEdit(dialog)
        layout.addWidget(url_input)

        submit_btn = QPushButton("Submit", dialog)
        submit_btn.clicked.connect(lambda: self.fetch_image_from_url(url_input.text(), dialog))
        layout.addWidget(submit_btn)

        dialog.exec_()

    def fetch_image_from_url(self, url, dialog):
        try:
            response = requests.get(url)
            response.raise_for_status()
            image_data = BytesIO(response.content)
            self.display_image(image_data)
            result = predict_image(image_url=url)
            if result:
                self.display_result(result)
            else:
                QMessageBox.warning(self, "Error", "Failed to get prediction results.")
            dialog.accept()
        except (UnidentifiedImageError, requests.exceptions.RequestException) as e:
            QMessageBox.warning(self, "Error", f"Failed to fetch image: {e}")

    def display_image(self, image_data):
        if isinstance(image_data, BytesIO):
            image = Image.open(image_data)
        else:
            image = Image.open(image_data)

        qt_image = ImageQt.ImageQt(image)
        pixmap = QPixmap.fromImage(qt_image)
        self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))

    def display_result(self, result):
        if result:
            predictions = result.get("predictions", [])
            if predictions:
                formatted_predictions = "\n".join([f"{item['tagName']}: {item['probability']*100:.2f}%" for item in predictions])
                self.result_label.setText(formatted_predictions)
                self.predictions = [(item['tagName'], item['probability']*100) for item in predictions]
                self.update_graph()
            else:
                self.result_label.setText("No predictions found.")
        else:
            self.result_label.setText("Failed to get predictions.")

    def update_graph(self):
        chart_type = self.chart_combo.currentText()
        ax = self.graph_canvas.figure.clear()

        if self.predictions:
            labels, probabilities = zip(*self.predictions)

            if chart_type == "Bar Graph":
                ax = self.graph_canvas.figure.add_subplot(111)
                ax.bar(labels, probabilities, color="skyblue")
                ax.set_ylabel("Probability (%)")
                ax.set_title("Prediction Results")

            elif chart_type == "Pie Chart":
                ax = self.graph_canvas.figure.add_subplot(111)
                ax.pie(probabilities, labels=labels, autopct="%1.1f%%", startangle=140)
                ax.set_title("Prediction Results")

        self.graph_canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
