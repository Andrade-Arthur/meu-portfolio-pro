from flask import Flask, render_template

app = Flask(__name__)

# Dados centralizados para todas as páginas (Portfolio e Currículos)
dados = {
    "nome": "Arthur Andrade",
    "cargo": "Desenvolvedor Fullstack",
    "email": "contactmeaaprofile@gmail.com",
    "bio": "Engenheiro de Software focado em construir arquiteturas robustas e interfaces fluidas. Especialista em escalabilidade, performance e código limpo.",
    "link_github": "https://github.com/Andrade-Arthur",
    "link_linkedin": "https://www.linkedin.com/in/arthur-andrade-5988133b6/",
    
    # Seus 3 projetos reais
    "projetos": [
        {"t": "Horror Game First Person", "d": "Projeto solo de um jogo de terror utilizando GDScript (Python Based).", "tag": "BACKEND / GAME DEV", "link": "https://github.com/Andrade-Arthur/Horror-game", "img": "GAME.jpg"},
        {"t": "Gestão Hospitalar", "d": "Simulação de modernização tecnológica de uma clínica médica com Python.", "tag": "BACKEND", "link": "https://github.com/Andrade-Arthur/ads-gestao-hospitalar", "img": "GH.jpg"},
        {"t": "Usabilidade e Redes", "d": "Aplicação de metodologias ágeis e infraestrutura de redes locais.", "tag": "REDES", "link": "https://github.com/Andrade-Arthur/ads-usabilidade-redes", "img": "redes.jpg"}
    ],
    
    # Skills organizadas para os ícones funcionarem em todas as páginas
    "skills": {
        "Backend": [
            {"n": "Python", "i": "python-plain"}, 
            {"n": "Flask", "i": "flask-original"}, 
            {"n": "Django", "i": "django-plain"}, 
            {"n": "Postgres", "i": "postgresql-plain"}
        ],
        "Frontend": [
            {"n": "React", "i": "react-original"}, 
            {"n": "Next.js", "i": "nextjs-original"}, 
            {"n": "Tailwind", "i": "tailwindcss-plain"},
            {"n": "TypeScript", "i": "typescript-plain"}
        ],
        "Ferramentas": [
            {"n": "Docker", "i": "docker-plain"}, 
            {"n": "Git", "i": "git-plain"}, 
            {"n": "AWS", "i": "amazonwebservices-plain-wordmark"}, 
            {"n": "Linux", "i": "linux-plain"}
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html', d=dados)

@app.route('/resume')
def live_resume():
    # Esta rota carrega o curriculo interativo (o que você mais gostou)
    return render_template('live_resume.html', d=dados)

@app.route('/download-cv')
def standard_cv():
    # Esta rota carrega a página branca de impressão
    return render_template('standard_cv.html', d=dados)

if __name__ == '__main__':
    app.run(debug=True)