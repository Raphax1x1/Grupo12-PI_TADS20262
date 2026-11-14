from decimal import Decimal, ROUND_HALF_UP
import os
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .aliquotas import CATEGORIAS_TRIBUTOS

app = FastAPI(
    title="API de Cálculo de Tributos Embutidos",
    description="Web API para cálculo de tributos embutidos por categoria.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/static",
    StaticFiles(
        directory=os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "frontend")
        )
    ),
    name="static",
)


def arredondar_moeda(valor: Decimal) -> Decimal:
  return valor.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


@app.get("/", response_class=HTMLResponse, summary="Página Principal da Interface")
def status_api():
  caminho_html = os.path.abspath(
      os.path.join(
          os.path.dirname(__file__), "..", "frontend", "index.html"
      )
  )
  if os.path.exists(caminho_html):
    with open(caminho_html, "r", encoding="utf-8") as f:
      return f.read()

  raise HTTPException(
      status_code=404, detail=f"Arquivo index.html não encontrado em: {caminho_html}"
  )


@app.get("/api/categorias", summary="Listar Categorias")
def listar_categorias():
  lista = []
  for chave, dados in CATEGORIAS_TRIBUTOS.items():
    lista.append(
        {"id": chave, "nome": dados["nome"], "descricao": dados["descricao"]}
    )
  return lista


@app.post("/api/calcular", summary="Calcular Tributos Embutidos")
async def simular_tributos(request: Request):
  # Lê os dados do corpo independentemente do formato (JSON ou Formulário)
  body = {}
  try:
    content_type = request.headers.get("content-type", "")
    if "application/json" in content_type:
      body = await request.json()
    elif "form" in content_type:
      form = await request.form()
      body = dict(form)
    else:
      try:
        body = await request.json()
      except Exception:
        body = dict(await request.form())
  except Exception:
    body = {}

  # Busca os valores aceitando múltiplas variações de nomes enviados pelo front
  categoria_id = (
      body.get("categoria_id") or body.get("categoria") or body.get("id")
  )
  preco_final = (
      body.get("preco_final")
      or body.get("preco")
      or body.get("valor")
      or body.get("precoFinal")
  )

  if not categoria_id:
    raise HTTPException(
        status_code=422,
        detail="O campo de categoria não foi informado corretamente.",
    )

  if preco_final is None:
    raise HTTPException(
        status_code=422, detail="O preço não foi informado corretamente."
    )

  categoria = CATEGORIAS_TRIBUTOS.get(categoria_id)
  if not categoria:
    raise HTTPException(
        status_code=404, detail="Categoria de produto não encontrada."
    )

  try:
    preco_str = str(preco_final).replace(",", ".")
    preco = Decimal(preco_str)
    if preco <= 0:
      raise ValueError()
  except Exception:
    raise HTTPException(
        status_code=422, detail="O preço informado é inválido."
    )

  aliquotas = categoria["aliquotas"]

  detalhamento = []
  total_impostos_valor = Decimal("0.00")
  total_impostos_percentual = Decimal("0.00")

  for tributo, aliquota in aliquotas.items():
    valor_tributo = arredondar_moeda(preco * aliquota)
    percentual_exibicao = (aliquota * Decimal("100")).quantize(Decimal("0.01"))

    total_impostos_valor += valor_tributo
    total_impostos_percentual += percentual_exibicao

    detalhamento.append({
        "tributo": tributo,
        "percentual": f"{percentual_exibicao}%",
        "valor_embutido": float(valor_tributo),
    })

  valor_liquido = arredondar_moeda(preco - total_impostos_valor)

  return {
      "categoria": categoria["nome"],
      "preco_final_informado": float(arredondar_moeda(preco)),
      "total_tributos_percentual": f"{total_impostos_percentual}%",
      "total_tributos_valor": float(total_impostos_valor),
      "valor_liquido_estimado": float(valor_liquido),
      "detalhamento_por_tributo": detalhamento,
  } 