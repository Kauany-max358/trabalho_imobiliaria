from flask import Flask, render_template, request, send_file
import csv
import os

app = Flask(__name__)

class Orcamento:
    def __init__(self, tipo, quartos, vagas, tem_criancas, parcelas_contrato):
        self.tipo = tipo
        self.quartos = int(quartos)
        self.vagas = int(vagas)
        self.tem_criancas = tem_criancas == 'Sim'
        self.parcelas_contrato = int(parcelas_contrato)
        self.valor_contrato_total = 2000.00

    def calcular_aluguel(self):
        valor_base = 0
        
        if self.tipo == 'Apartamento':
            valor_base = 700.00
            if self.quartos >= 2: 
                valor_base += 200.00
            if self.vagas > 0: 
                valor_base += 300.00
            if not self.tem_criancas:
                valor_base *= 0.95

        elif self.tipo == 'Casa':
            valor_base = 900.00
            if self.quartos >= 2: 
                valor_base += 250.00
            if self.vagas > 0: 
                valor_base += 300.00

        elif self.tipo == 'Estudio':
            valor_base = 1200.00
            if self.vagas >= 2:
                valor_base += 250.00 + ((self.vagas - 2) * 60.00)
        
        return valor_base

    def calcular_parcela_contrato(self):
        # Valor do contrato fixo de R$ 2.000,00 
        return self.valor_contrato_total / self.parcelas_contrato

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        quartos = request.form.get('quartos', 0)
        vagas = request.form.get('vagas', 0)
        criancas = request.form.get('criancas', 'Sim')
        parcelas = request.form.get('parcelas', 1)

        orc = Orcamento(tipo, quartos, vagas, criancas, parcelas)
        
        aluguel = orc.calcular_aluguel()
        parcela_contrato = orc.calcular_parcela_contrato()
        total_mensal = aluguel + parcela_contrato

        # Gerar o CSV com as 12 parcelas 
        caminho_csv = 'orcamento_detalhado.csv'
        with open(caminho_csv, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Parcela', 'Descricao', 'Valor Mensal'])
            for i in range(1, 13):
                # A parcela do contrato só aparece até o limite escolhido (5x)
                valor_final_mes = aluguel + (parcela_contrato if i <= int(parcelas) else 0)
                writer.writerow([i, f'Aluguel {tipo}', f'R$ {valor_final_mes:.2f}'])

        return render_template('index.html', 
                               resultado=True, 
                               aluguel=aluguel, 
                               contrato=parcela_contrato, 
                               total=total_mensal, 
                               parcelas=parcelas)

    return render_template('index.html', resultado=False)

if __name__ == '__main__':
    app.run(debug=True)