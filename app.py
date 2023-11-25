from flask import Flask, render_template, request

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

if __name__ == '__main__':
    app.run(debug=True)
