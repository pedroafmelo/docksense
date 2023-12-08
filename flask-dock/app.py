from flask import Flask, render_template, request


app = Flask(__name__)

chat_history = []
gpt_respostas = ["Com base nos comentários analisados na Glassdoor, o principal problema visto na empresa Dock é a falta de transparência e a mudança constante de objetivos, estratégias e direcionamentos. Além disso, há relatos de lideranças despreparadas para exercer seus cargos, falta de comunicação eficiente, falta de clareza das atividades e ausência de processos bem definidos. Esses problemas podem gerar desmotivação, falta de confiança e dificuldades na organização e no crescimento profissional dos colaboradores.", "Com base nos comentários disponibilizados na Glassdoor, podemos identificar alguns pontos que podem ser melhorados para aumentar a satisfação dos colaboradores na empresa Dock:\n\n1. Melhorar a gestão de equipes: Vários comentários mencionam a falta de qualificação e capacidade de liderança em certos cargos. Investir em treinamentos direcionados para as lideranças, especialmente nas lideranças mais novas, pode ajudar a melhorar a gestão de equipes.\n\n2. Fomentar a transparência e a comunicação interna: Vários comentários mencionam a falta de transparência por parte da alta direção e a falta de clareza nas atividades. Realizar reuniões regulares para atualizar os colaboradores sobre estratégias, caminhos e mudanças pode ajudar a melhorar a transparência e a comunicação interna.\n\n3. Melhorar a organização e os processos internos: Alguns comentários mencionam problemas de organização, falta de processos e mudanças constantes de rumo. Investir em melhorias na organização interna, definir planos estratégicos com contingências e estabelecer processos mais sólidos podem ajudar a melhorar a eficiência das atividades.\n\n4. Valorizar e reconhecer os colaboradores: Alguns comentários mencionam a falta de valorização dos colaboradores e a falta de oportunidades de crescimento. Criar um ambiente que valorize e reconheça os esforços dos colaboradores, oferecer oportunidades de crescimento e estabelecer critérios objetivos para avaliações de desempenho podem contribuir para aumentar a satisfação dos colaboradores.\n\n5. Promover uma cultura saudável e inclusiva: Alguns comentários mencionam problemas como assédio, perseguição e falta de respeito. Investir em treinamentos sobre diversidade, inclusão e respeito no ambiente de trabalho, além de adotar políticas claras de combate a esses problemas, pode contribuir para promover uma cultura saudável e inclusiva na empresa.\n\nEssas são algumas sugestões com base nos comentários mencionados. É importante ressaltar que a empresa deve analisar esses pontos com mais detalhes, buscar feedbacks dos colaboradores e implementar as ações adequadas de acordo com sua realidade e objetivos."]

@app.route('/chatbot/', methods=['GET'])
def chatbot():
    return render_template('chatbot.html', chat_history=chat_history)

@app.route('/chatbot/', methods=['POST'])
def send_message():
    message = request.form['message']
    is_question = True 
    
    chat_history.append(('Usuario: '+message, is_question))
    chat_history.append(('DockSense: ' + gpt_respostas.pop(), False))

    return chatbot()

if __name__ == '__main__':
    app.run() 