from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def calculate_time_values(total_time, percentages):
    return [total_time * p / 100 for p in percentages]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        total_time = int(request.form['total_time'])
        section_1_percentage = int(request.form['section_1_time'])
        section_2_percentage = int(request.form['section_2_time'])
        section_3_percentage = int(request.form['section_3_time'])
        section_1_labor = int(request.form['section_1_labor'])
        section_2_labor = int(request.form['section_2_labor'])
        section_3_labor = int(request.form['section_3_labor'])

        section_times = calculate_time_values(total_time, [section_1_percentage, section_2_percentage, section_3_percentage])
        section_labors = [section_1_labor, section_2_labor, section_3_labor]

        return render_template('result.html', total_time=total_time, section_times=section_times, section_labors=section_labors)

    return render_template('index.html')





import random

# Sample employee dictionary with Indian names
employee_dict = {
    1: {'id': 1, 'name': 'Aditi Musunur', 'email': 'aditi@example.com', 'available': random.choice([True, False])},
    2: {'id': 2, 'name': 'Advitiya Sujeet', 'email': 'advitiya@example.com', 'available': random.choice([True, False])},
    3: {'id': 3, 'name': 'Alagesan Poduri', 'email': 'alagesan@example.com', 'available': random.choice([True, False])},
    4: {'id': 4, 'name': 'Amrish Ilyas', 'email': 'amrish@example.com', 'available': random.choice([True, False])},
    5: {'id': 5, 'name': 'Aprativirya Seshan', 'email': 'apravitirya@example.com', 'available': random.choice([True, False])},
    6: {'id': 6, 'name': 'Asvathama Ponnada', 'email': 'asvathama@example.com', 'available': random.choice([True, False])},
    7: {'id': 7, 'name': 'Avantas Ghosal', 'email': 'avantas@example.com', 'available': random.choice([True, False])},
    8: {'id': 8, 'name': 'Avidosa Vaisakhi', 'email': 'avidosavaisakhi@example.com', 'available': random.choice([True, False])},
    9: {'id': 9, 'name': 'Barsati Sandipa', 'email': 'barsati@example.com', 'available': random.choice([True, False])},
    10: {'id': 10, 'name': 'Debasis Sundhararajan', 'email': 'debasiss@example.com', 'available': random.choice([True, False])},
    11: {'id': 11, 'name': 'Devasru Subramanyan', 'email': 'devasru@example.com', 'available': random.choice([True, False])},
    12: {'id': 12, 'name': 'Dharmadhrt Ramila', 'email': 'dharmadhrt@example.com', 'available': random.choice([True, False])},
    13: {'id': 13, 'name': 'Dhritiman Salim', 'email': 'dhritiman@example.com', 'available': random.choice([True, False])},
    14: {'id': 14, 'name': 'Gopa Trilochana', 'email': 'gopa@example.com', 'available': random.choice([True, False])},
    15: {'id': 15, 'name': 'Hardeep Suksma', 'email': 'hardeep@example.com', 'available': random.choice([True, False])},
    16: {'id': 16, 'name': 'Jayadev Mitali', 'email': 'jayadev@example.com', 'available': random.choice([True, False])},
    17: {'id': 17, 'name': 'Jitendra Choudhary', 'email': 'jitendra@example.com', 'available': random.choice([True, False])},
    18: {'id': 18, 'name': 'Kalyanavata Veerender', 'email': 'kalyanavata@example.com', 'available': random.choice([True, False])},
    19: {'id': 19, 'name': 'Naveen Tikaram', 'email': 'naveen@example.com', 'available': random.choice([True, False])},
    20: {'id': 20, 'name': 'Vijai Sritharan', 'email': 'vijai@example.com', 'available': random.choice([True, False])},
    # Add 5 more employees with similar details
    21: {'id': 21, 'name': 'Employee 21', 'email': 'employee21@example.com', 'available': random.choice([True, False])},
    22: {'id': 22, 'name': 'Employee 22', 'email': 'employee22@example.com', 'available': random.choice([True, False])},
    23: {'id': 23, 'name': 'Employee 23', 'email': 'employee23@example.com', 'available': random.choice([True, False])},
    24: {'id': 24, 'name': 'Employee 24', 'email': 'employee24@example.com', 'available': random.choice([True, False])},
    25: {'id': 25, 'name': 'Employee 25', 'email': 'employee25@example.com', 'available': random.choice([True, False])},
}

print(employee_dict)

@app.route('/emp', methods=['GET', 'POST'])
def emp():
    return render_template('employee_db.html', employees=employee_dict.values())

@app.route('/update_employee/<int:employee_id>', methods=['POST'])
def update_employee(employee_id):
    if request.method == 'POST':
        print(f"Received POST request for employee {employee_id}")
        print(f"Form data: {request.form}")
        # Update the 'available' status in the employee_dict
        employee_dict[employee_id]['available'] = bool(request.form.get('available'))
        # You can perform any additional logic or database updates here

    # Pass the updated employee dictionary to the template
    return render_template('employee_db.html', employees=employee_dict.values())



if __name__ == '__main__':
    app.run(debug=True)
