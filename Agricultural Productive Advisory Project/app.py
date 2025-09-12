from flask import Flask, render_template, request
import pandas as pd
from scipy.optimize import linprog

app = Flask(__name__)

def optimize_crops(total_hectares, max_cost, number_of_crops):
    excel_file_path = "C:/Users/joses/OneDrive/Desktop/TP3_Tesis/Base_Optimizacion.xlsx"

    data = pd.read_excel(excel_file_path)
    
    # Costos e ingresos por hectárea
    data['Costo total por hectárea'] = data['Max Cost (USD)xHectarea'] + \
                                      data['Costo Setup Riego USD por Hectárea'] + \
                                      data['Costo riego mensual X hect']
    data['Ingresos por hectárea'] = data['Produccion en los 10 años (kg) x hect'] * data['Precio por kg']

    # Seleccion de los cultivos con mayores ingresos por hectárea
    top_crops = data.nlargest(number_of_crops, 'Ingresos por hectárea')

    # Coeficientes para la función objetivo (max ingresos)
    c = -top_crops['Ingresos por hectárea'].values  # Negativo porque linprog minimiza

    # Restricciones: asignación equitativa de hectáreas si es requerido o variable entre 0 y total_hectares
    bounds = [(0, total_hectares / number_of_crops) for _ in range(number_of_crops)]

    # Restricción de desigualdad para el presupuesto
    A_ub = [top_crops['Costo total por hectárea'].values]  # Coefs de costo
    b_ub = [max_cost]  # El costo total no puede exceder el presupuesto

    # Optimización usando linprog
    opt_result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

    if opt_result.success:
        # Nombres de los cultivos y detalles de la solución
        top_crops['Hectáreas asignadas'] = opt_result.x
        top_crops['Producción estimada en 10 años (kg)'] = \
            top_crops['Produccion en los 10 años (kg) x hect'] * top_crops['Hectáreas asignadas']
        top_crops['Ingreso potencial en 10 años (USD)'] = \
            top_crops['Producción estimada en 10 años (kg)'] * top_crops['Precio por kg']
        top_crops['Costo total estimado (USD)'] = \
            top_crops['Costo total por hectárea'] * top_crops['Hectáreas asignadas']

        # Resultados como DF
        return top_crops[['Item', 'Hectáreas asignadas', 'Producción estimada en 10 años (kg)',
                          'Ingreso potencial en 10 años (USD)', 'Costo total estimado (USD)']]
    else:
        return "Optimization was unsuccessful. Please check the inputs and constraints."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/optimize', methods=['POST'])
def optimize():
    total_hectares = int(request.form['total_hectares'])
    max_cost = float(request.form['max_cost'])
    number_of_crops = int(request.form['number_of_crops'])
    result = optimize_crops(total_hectares, max_cost, number_of_crops)
    return result.to_html() if isinstance(result, pd.DataFrame) else result

if __name__ == '__main__':
    app.run(debug=True)
