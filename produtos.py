from flask import Flask, jsonify

produtos = [
  { "codigo": "HF001", "nome": "Banana prata",       "categoria": "fruta",   "preco": 7.90,  "imagem": null, "status": "ativo" },
  { "codigo": "HF002", "nome": "Banana da terra",    "categoria": "fruta",   "preco": 9.50,  "imagem": null, "status": "ativo" },
  { "codigo": "HF003", "nome": "Maçã gala",          "categoria": "fruta",   "preco": 8.99,  "imagem": null, "status": "ativo" },
  { "codigo": "HF004", "nome": "Maçã fuji",          "categoria": "fruta",   "preco": 9.49,  "imagem": null, "status": "ativo" },
  { "codigo": "HF005", "nome": "Laranja pera",       "categoria": "fruta",   "preco": 4.50,  "imagem": null, "status": "ativo" },
  { "codigo": "HF006", "nome": "Limão tahiti",       "categoria": "fruta",   "preco": 6.90,  "imagem": null, "status": "ativo" },
  { "codigo": "HF007", "nome": "Tomate italiano",    "categoria": "legume",  "preco": 8.90,  "imagem": null, "status": "ativo" },
  { "codigo": "HF008", "nome": "Tomate cereja",      "categoria": "legume",  "preco": 24.90, "imagem": null, "status": "ativo" },
  { "codigo": "HF009", "nome": "Batata inglesa",     "categoria": "legume",  "preco": 5.99,  "imagem": null, "status": "ativo" },
  { "codigo": "HF010", "nome": "Batata doce",        "categoria": "legume",  "preco": 6.49,  "imagem": null, "status": "ativo" },
  { "codigo": "HF011", "nome": "Cenoura",            "categoria": "legume",  "preco": 4.99,  "imagem": null, "status": "ativo" },
  { "codigo": "HF012", "nome": "Abobrinha italiana", "categoria": "legume",  "preco": 7.50,  "imagem": null, "status": "ativo" },
  { "codigo": "HF013", "nome": "Alface crespa",      "categoria": "verdura", "preco": 3.50,  "imagem": null, "status": "ativo" },
  { "codigo": "HF014", "nome": "Alface americana",   "categoria": "verdura", "preco": 4.90,  "imagem": null, "status": "ativo" },
  { "codigo": "HF015", "nome": "Couve manteiga",     "categoria": "verdura", "preco": 3.20,  "imagem": null, "status": "ativo" }
]