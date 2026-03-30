from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    dados = {
        "nome": "Arthur Andrade",
        "cargo": "Desenvolvedor Fullstack",
        "email": "contactmeaaprofile@gmail.com",
        "bio": "Fullstack Engineer focado na arquitetura de sistemas escaláveis e interfaces de alta fidelidade. Especialista em traduzir lógica de backend complexa em soluções resilientes, operando sob os mais rigorosos padrões de Clean Code e performance.",
        "link_github": "https://github.com/Andrade-Arthur",
        "link_linkedin": "https://www.linkedin.com/in/arthur-andrade-5988133b6/",
        "experiencia": "02+",
        "projetos_concluidos": "15+",
        "clientes": "10+",
        "processo": [
            {"num": "01", "titulo": "Requisitos", "desc": "Análise profunda das necessidades."},
            {"num": "02", "titulo": "Arquitetura", "desc": "Design de sistemas escaláveis."},
            {"num": "03", "titulo": "Execução", "desc": "Interfaces modernas e alta performance."}
        ],
        "projetos": [
            {"t": "Horror Game First Person", "d": "Um Projeto First Person criado com o tema horror utilizando GD SCRIPT.", "tag": "BACKEND", "link": "https://github.com/Andrade-Arthur/Horror-game", "img": "GAME.jpg"},
            {"t": "Gestão Hospitalar", "d": "Simulação de modernização tecnológica de uma clínica médica.", "tag": "BACKEND", "link": "https://github.com/Andrade-Arthur/ads-gestao-hospitalar", "img": "GH.jpg"},
            {"t": "Usabilidade e Redes", "d": "Aplicação de metodologias ágeis e infraestrutura de redes locais.", "tag": "REDES", "link": "https://github.com/Andrade-Arthur/ads-usabilidade-redes", "img": "redes.jpg"}
        ],
        "skills": {
            "Backend": [
                {"n": "Python", "i": "python-plain"},
                {"n": "Flask", "i": "flask-original"},
                {"n": "Django", "i": "django-plain"},
                {"n": "Postgres", "i": "postgresql-plain"},
                {"n": "Node.js", "i": "nodejs-plain"},
                {"n": "Redis", "i": "redis-plain"}
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
                {"n": "Linux", "i": "linux-plain"},
                {"n": "CI/CD", "i": "githubactions-plain"},
                {"n": "GDScript", "i": "godot-plain"}
            ]
        }
    }
    return render_template('index.html', d=dados)

if __name__ == '__main__':
    app.run(debug=True)