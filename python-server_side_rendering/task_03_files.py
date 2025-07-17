from flask import Flask, render_template, request
import json
import csv
import logging
import sqlite3

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def json_file():
	filename = 'products.json'
	try:
		with open(filename, "r") as file:
			return json.load(file)
	except Exception as e:
		logging.error('Something went wrong')
		return None

def csv_file():
	filename = 'products.csv'
	data_list = []
	try:
		with open(filename, "r", newline='', encoding='utf-8') as file:
			reader_dict = csv.DictReader(file)
			for row in reader_dict:
				row['id'] = int(row['id'])
				row['name'] = str(row['name'])
				row['category'] = str(row['category'])
				row['price'] = float(row['price'])
				data_list.append(row)
		return data_list

	except FileNotFoundError:
		logging.error(f"CSV file not found")
		return None

	except Exception as e:
		logging.error('Something went wrong')
		return None

def sql_file():
	db = sqlite3.connect("products.db")
	cursor = db.cursor()
	cursor.execute("SELECT id, name, category, price FROM products")
	data = cursor.fetchall()
	db.close()
	for row in data:
		return row


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/items')
def item():
	filename = 'items.json'
	with open(filename, "r") as file:
		data = json.load(file)
		list_items = data.get("items")
	return render_template('items.html', items=list_items)

@app.route('/products')
def display_product():
	source_format = request.args.get('source')
	given_id = request.args.get('id')
	data = None
	error_msg = None

	if source_format == 'json':
		data = json_file()

	elif source_format == 'csv':
		data = csv_file()

	elif source_format == 'sql':
		data = sql_file()

	else:
		error_msg = 'Wrong source, please use "json", "csv" or "sql" files'

	if error_msg:
		return render_template('product_display.html', error=error_msg)

	if not data:
		error_msg = 'Data not found'
		return render_template('product_display.html', error=error_msg)

	if given_id:
		try:
			given_id = int(given_id)
			found_product = None
			for product in data:
				if product['id'] == given_id:
					found_product = product
					break
			if found_product:
				return render_template('product_display.html', products=[found_product])
			else:
				error_msg = 'No product with this ID was found'
				return render_template('product_display.html', error=error_msg)

		except ValueError:
			error_msg = 'Invalid ID format. ID must be an integer'
			return render_template('product_display.html', error=error_msg)
	else:
		return render_template('product_display.html', products=data)

if __name__ == '__main__':
	app.run(debug=True, port=5000)
