from decimal import Decimal

# Alíquotas armazenadas como fração decimal (ex: 0.07 = 7%)
# Valores baseados na tabela de setores e regras fiscais
CATEGORIAS_TRIBUTOS = {
    "hortifruti_in_natura": {
        "nome": "1. Feira (Hortifrúti In Natura)",
        "descricao": "Isenção de ICMS e Alíquota Zero de PIS/COFINS (Convênio 44/75 e Lei 10.865/04)",
        "aliquotas": {
            "ICMS": Decimal("0.00"),
            "PIS": Decimal("0.00"),
            "COFINS": Decimal("0.00"),
            "ISS": Decimal("0.00"),
        },
    },
    "pereciveis": {
        "nome": "2. Perecíveis (Frios, Laticínios, Carnes)",
        "descricao": "Regime misto com isenção/redução ou ICMS-ST",
        "aliquotas": {
            "ICMS": Decimal("0.07"),
            "PIS": Decimal("0.0165"),
            "COFINS": Decimal("0.076"),
            "ISS": Decimal("0.00"),
        },
    },
    "mercearia": {
        "nome": "3. Mercearia (Secos, Bebidas, Limpeza)",
        "descricao": "Cesta básica, itens monofásicos e tributados",
        "aliquotas": {
            "ICMS": Decimal("0.18"),
            "PIS": Decimal("0.0165"),
            "COFINS": Decimal("0.076"),
            "ISS": Decimal("0.00"),
        },
    },
    "auto_pecas": {
        "nome": "4. Peças de Automóveis (Autopeças)",
        "descricao": "Sujeito a ICMS-ST e Tributação Monofásica",
        "aliquotas": {
            "ICMS": Decimal("0.18"),
            "PIS": Decimal("0.0065"),
            "COFINS": Decimal("0.03"),
            "ISS": Decimal("0.00"),
        },
    },
    "bebidas_frias_alcoolicas": {
        "nome": "5. Bebidas (Frias e Alcoólicas)",
        "descricao": "ICMS-ST e Monofásico/Tributado",
        "aliquotas": {
            "ICMS": Decimal("0.20"),
            "PIS": Decimal("0.02"),
            "COFINS": Decimal("0.096"),
            "ISS": Decimal("0.00"),
        },
    },
    "limpeza_higiene": {
        "nome": "6. Limpeza e Higiene Pessoal (Perfumaria)",
        "descricao": "ICMS-ST predominante e Monofásico para higiene",
        "aliquotas": {
            "ICMS": Decimal("0.18"),
            "PIS": Decimal("0.021"),
            "COFINS": Decimal("0.099"),
            "ISS": Decimal("0.00"),
        },
    },
    "padaria_confeitaria": {
        "nome": "7. Padaria e Confeitaria",
        "descricao": "Itens da cesta (pão francês) e produtos tributados/ST",
        "aliquotas": {
            "ICMS": Decimal("0.12"),
            "PIS": Decimal("0.0165"),
            "COFINS": Decimal("0.076"),
            "ISS": Decimal("0.00"),
        },
    },
    "medicamentos": {
        "nome": "8. Medicamentos e Farmácia",
        "descricao": "100% ICMS-ST e Monofásico (Listas Positiva/Negativa)",
        "aliquotas": {
            "ICMS": Decimal("0.18"),
            "PIS": Decimal("0.021"),
            "COFINS": Decimal("0.099"),
            "ISS": Decimal("0.00"),
        },
    },
    "material_construcao": {
        "nome": "9. Material de Construção e Ferragens",
        "descricao": "Presença de ICMS-ST e tributação normal",
        "aliquotas": {
            "ICMS": Decimal("0.18"),
            "PIS": Decimal("0.0165"),
            "COFINS": Decimal("0.076"),
            "ISS": Decimal("0.00"),
        },
    },
    "vestuario": {
        "nome": "10. Vestuário, Calçados e Acessórios",
        "descricao": "Tributação integral padrão sem regime ST na maioria",
        "aliquotas": {
            "ICMS": Decimal("0.18"),
            "PIS": Decimal("0.0165"),
            "COFINS": Decimal("0.076"),
            "ISS": Decimal("0.00"),
        },
    },
    "eletronicos": {
        "nome": "11. Eletrônicos, Celulares e Eletrodomésticos",
        "descricao": "Quase todos os itens com ICMS-ST (Segmento 21 CEST)",
        "aliquotas": {
            "ICMS": Decimal("0.18"),
            "PIS": Decimal("0.0165"),
            "COFINS": Decimal("0.076"),
            "ISS": Decimal("0.00"),
        },
    },
    "pet_shop": {
        "nome": "12. Pet Shop (Ração e Acessórios)",
        "descricao": "ICMS-ST para rações e tributado para acessórios",
        "aliquotas": {
            "ICMS": Decimal("0.18"),
            "PIS": Decimal("0.0165"),
            "COFINS": Decimal("0.076"),
            "ISS": Decimal("0.00"),
        },
    },
    "combustiveis": {
        "nome": "13. Combustíveis e Lubrificantes",
        "descricao": "Tributação monofásica de ICMS e PIS/COFINS",
        "aliquotas": {
            "ICMS": Decimal("0.12"),
            "PIS": Decimal("0.01"),
            "COFINS": Decimal("0.04"),
            "ISS": Decimal("0.00"),
        },
    },
    "papelaria": {
        "nome": "14. Papelaria e Bazar (Utilidades)",
        "descricao": "ICMS-ST em materiais escolares e imunidade em livros",
        "aliquotas": {
            "ICMS": Decimal("0.18"),
            "PIS": Decimal("0.0165"),
            "COFINS": Decimal("0.076"),
            "ISS": Decimal("0.00"),
        },
    },
}