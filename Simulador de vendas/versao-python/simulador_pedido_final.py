import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime

# DADOS BASE 

TABELAS_PRECO = [
    "001 - PADRAO",
]

CONDICOES_DESCONTO = {
    "Sem Desconto (À Vista / Padrão)": 0.00,
    "A VISTA 05%": 5.00,
    "A VISTA 08%": 8.00,
    "A VISTA 10%": 10.00,
}

PRODUTOS = [

    # CAIXA DE 10 LITROS
{"codigo": "209", "nome": "Fruta Dourada", "preco": 95.00, "grupo": "CAIXA DE 10 LITROS"},
{"codigo": "211", "nome": "Doce Imperial", "preco": 95.00, "grupo": "CAIXA DE 10 LITROS"},
{"codigo": "212", "nome": "Brigadeiro Real", "preco": 95.00, "grupo": "CAIXA DE 10 LITROS"},
{"codigo": "213", "nome": "Nuvem Doce", "preco": 95.00, "grupo": "CAIXA DE 10 LITROS"},
{"codigo": "214", "nome": "Coco Tropical", "preco": 95.00, "grupo": "CAIXA DE 10 LITROS"},
{"codigo": "215", "nome": "Fruta do Sertão", "preco": 95.00, "grupo": "CAIXA DE 10 LITROS"},
{"codigo": "216", "nome": "Chocolate Supremo", "preco": 95.00, "grupo": "CAIXA DE 10 LITROS"},
{"codigo": "217", "nome": "Creme Dourado", "preco": 95.00, "grupo": "CAIXA DE 10 LITROS"},
{"codigo": "218", "nome": "Mix Tropical", "preco": 95.00, "grupo": "CAIXA DE 10 LITROS"},
{"codigo": "219", "nome": "Crocante Suave", "preco": 95.00, "grupo": "CAIXA DE 10 LITROS"},
{"codigo": "220", "nome": "Fruta Silvestre", "preco": 95.00, "grupo": "CAIXA DE 10 LITROS"},
{"codigo": "222", "nome": "Chocolate Intenso", "preco": 95.00, "grupo": "CAIXA DE 10 LITROS"},
{"codigo": "223", "nome": "Morango Cremoso", "preco": 95.00, "grupo": "CAIXA DE 10 LITROS"},
{"codigo": "224", "nome": "Trio Especial", "preco": 95.00, "grupo": "CAIXA DE 10 LITROS"},
{"codigo": "225", "nome": "Creme Rosado", "preco": 95.00, "grupo": "CAIXA DE 10 LITROS"},

# ARROZ DE 1KG
{"codigo": "52084", "nome": "Arroz Branco Tipo 1", "preco": 6.90, "grupo": "PACOTE DE 01 KG"},
{"codigo": "52077", "nome": "Arroz Integral", "preco": 7.50, "grupo": "PACOTE DE 01 KG"},
{"codigo": "52091", "nome": "Arroz Parboilizado", "preco": 7.20, "grupo": "PACOTE DE 01 KG"},
{"codigo": "52107", "nome": "Arroz Arbóreo", "preco": 14.90, "grupo": "PACOTE DE 01 KG"},
{"codigo": "52114", "nome": "Arroz Cateto", "preco": 9.90, "grupo": "PACOTE DE 01 KG"},

# FEIJÃO 1KG
{"codigo": "53001", "nome": "Feijão Carioca Tipo 1", "preco": 8.50, "grupo": "PACOTE DE 01 KG"},
{"codigo": "53002", "nome": "Feijão Preto", "preco": 8.90, "grupo": "PACOTE DE 01 KG"},
{"codigo": "53003", "nome": "Feijão Fradinho", "preco": 9.50, "grupo": "PACOTE DE 01 KG"},
{"codigo": "53004", "nome": "Feijão Macassar", "preco": 9.20, "grupo": "PACOTE DE 01 KG"},
{"codigo": "53005", "nome": "Feijão Branco", "preco": 12.90, "grupo": "PACOTE DE 01 KG"},

# MACARRÃO
{"codigo": "54001", "nome": "Macarrão Espaguete", "preco": 4.50, "grupo": "PACOTE DE 500 GRAMAS"},
{"codigo": "54002", "nome": "Macarrão Parafuso", "preco": 4.90, "grupo": "PACOTE DE 500 GRAMAS"},
{"codigo": "54003", "nome": "Macarrão Penne", "preco": 5.50, "grupo": "PACOTE DE 500 GRAMAS"},
{"codigo": "54004", "nome": "Macarrão Padre Nosso", "preco": 4.20, "grupo": "PACOTE DE 500 GRAMAS"},
{"codigo": "54005", "nome": "Macarrão Talharim", "preco": 5.90, "grupo": "PACOTE DE 500 GRAMAS"},

# AÇUCAR 1KG
{"codigo": "55001", "nome": "Açúcar Cristal", "preco": 4.50, "grupo": "PACOTE DE 01 KG"},
{"codigo": "55002", "nome": "Açúcar Refinado", "preco": 5.20, "grupo": "PACOTE DE 01 KG"},
{"codigo": "55003", "nome": "Açúcar Demerara", "preco": 7.90, "grupo": "PACOTE DE 01 KG"},
{"codigo": "55004", "nome": "Açúcar Mascavo", "preco": 8.50, "grupo": "PACOTE DE 01 KG"},
{"codigo": "55005", "nome": "Açúcar de Confeiteiro", "preco": 9.90, "grupo": "PACOTE DE 500 GRAMAS"},

# SAL 1KG
{"codigo": "56001", "nome": "Sal Refinado", "preco": 2.50, "grupo": "PACOTE DE 01 KG"},
{"codigo": "56002", "nome": "Sal Grosso", "preco": 3.90, "grupo": "PACOTE DE 01 KG"},
{"codigo": "56004", "nome": "Sal Light", "preco": 8.90, "grupo": "PACOTE DE 500 GRAMAS"},
{"codigo": "56005", "nome": "Sal Rosa do Himalaia", "preco": 12.90, "grupo": "PACOTE DE 500 GRAMAS"},

# ÓLEO
{"codigo": "58001", "nome": "Óleo de Soja", "preco": 7.90, "grupo": "GARRAFA DE 900 ML"},
{"codigo": "58002", "nome": "Óleo de Girassol", "preco": 11.90, "grupo": "GARRAFA DE 900 ML"},
{"codigo": "58004", "nome": "Azeite de Oliva", "preco": 29.90, "grupo": "GARRAFA DE 500 ML"},
{"codigo": "58005", "nome": "Óleo de Canola", "preco": 13.90, "grupo": "GARRAFA DE 900 ML"},

# PICOLÉ SUBLIME cx c/ 20 unid.
{"codigo": "59001", "nome": "Café Tradicional", "preco": 18.90, "grupo": "PACOTE DE 250 GRAMAS"},
{"codigo": "59002", "nome": "Café Extraforte", "preco": 19.90, "grupo": "PACOTE DE 250 GRAMAS"},
{"codigo": "59003", "nome": "Café Gourmet", "preco": 27.90, "grupo": "PACOTE DE 250 GRAMAS"},
{"codigo": "59004", "nome": "Achocolatado em Pó", "preco": 8.90, "grupo": "PACOTE DE 400 GRAMAS"},
{"codigo": "59005", "nome": "Chocolate em Pó", "preco": 12.90, "grupo": "PACOTE DE 200 GRAMAS"},

# BISCOITOS
{"codigo": "60001", "nome": "Biscoito Cream Cracker", "preco": 5.50, "grupo": "PACOTE DE 350 GRAMAS"},
{"codigo": "60002", "nome": "Biscoito Maisena", "preco": 5.90, "grupo": "PACOTE DE 350 GRAMAS"},
{"codigo": "60003", "nome": "Biscoito Recheado Chocolate", "preco": 3.50, "grupo": "PACOTE DE 120 GRAMAS"},
{"codigo": "60004", "nome": "Biscoito Recheado Morango", "preco": 3.50, "grupo": "PACOTE DE 120 GRAMAS"},
{"codigo": "60005", "nome": "Biscoito Wafer", "preco": 4.50, "grupo": "PACOTE DE 110 GRAMAS"}
]

GRUPOS = sorted(set(p["grupo"] for p in PRODUTOS))


def formatar_moeda(valor: float) -> str:
    """Formata valor float como R$ 0.000,00 (padrão brasileiro)."""
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


class SimuladorVendas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulação de Vendas")
        self.geometry("620x780")
        self.minsize(560, 700)
        self.configure(bg="#f5f6f8")

        self.itens = []  # lista de dicts: codigo, nome, preco, quantidade, subtotal

        self._construir_interface()

    # ------------------------------------------------------------------
    # INTERFACE
    # ------------------------------------------------------------------
    def _construir_interface(self):
        pad = {"padx": 16, "pady": 6}

        titulo = tk.Label(
            self, text="Simulação de Vendas", font=("Segoe UI", 18, "bold"),
            bg="#f5f6f8", fg="#1f2933"
        )
        titulo.pack(anchor="w", padx=16, pady=(16, 8))

        container = ttk.Frame(self)
        container.pack(fill="both", expand=True, padx=4)

        # --- Nome do Cliente -------------------------------------------------
        ttk.Label(container, text="Nome do Cliente").pack(anchor="w", **pad)
        self.entry_cliente = ttk.Entry(container)
        self.entry_cliente.pack(fill="x", padx=16)

        # --- Tabela de Preço ---------------------------------------------------
        ttk.Label(container, text="Tabela de Preço").pack(anchor="w", **pad)
        self.combo_tabela = ttk.Combobox(
            container, values=TABELAS_PRECO, state="readonly"
        )
        self.combo_tabela.current(0)
        self.combo_tabela.pack(fill="x", padx=16)

        # --- Condição de Desconto ----------------------------------------------
        ttk.Label(container, text="Condição de Desconto").pack(anchor="w", **pad)
        self.combo_desconto = ttk.Combobox(
            container, values=list(CONDICOES_DESCONTO.keys()), state="readonly"
        )
        self.combo_desconto.current(0)
        self.combo_desconto.pack(fill="x", padx=16)
        self.combo_desconto.bind("<<ComboboxSelected>>", lambda e: self._atualizar_totais())

        # --- Escolha os Itens ----------------------------------------------------
        frame_itens = ttk.LabelFrame(container, text=" Escolha os Itens ")
        frame_itens.pack(fill="x", padx=16, pady=(16, 6))

        ttk.Label(frame_itens, text="Grupo").pack(anchor="w", padx=10, pady=(8, 2))
        self.combo_grupo = ttk.Combobox(
            frame_itens,
            values=GRUPOS,
            state="readonly",
        )
        self.combo_grupo.pack(fill="x", padx=10)
        self.combo_grupo.bind("<<ComboboxSelected>>", self._atualizar_produtos)

        ttk.Label(frame_itens, text="Produto").pack(anchor="w", padx=10, pady=(10, 2))
        self.combo_produto = ttk.Combobox(
            frame_itens,
            state="readonly",
        )
        self.combo_produto.pack(fill="x", padx=10)

        if GRUPOS:
            self.combo_grupo.current(0)
            self._atualizar_produtos()

        linha_qtd = ttk.Frame(frame_itens)
        linha_qtd.pack(fill="x", padx=10, pady=(10, 10))

        col_qtd = ttk.Frame(linha_qtd)
        col_qtd.pack(side="left", fill="x", expand=True)
        ttk.Label(col_qtd, text="Quantidade").pack(anchor="w")
        self.entry_quantidade = ttk.Entry(col_qtd)
        self.entry_quantidade.insert(0, "1")
        self.entry_quantidade.pack(fill="x")

        btn_adicionar = tk.Button(
            linha_qtd, text="+ Adicionar Item", bg="#2f80ed", fg="white",
            relief="flat", font=("Segoe UI", 10, "bold"),
            command=self._adicionar_item, padx=14, pady=8
        )
        btn_adicionar.pack(side="right", padx=(10, 0), pady=(18, 0))

        # --- Itens Adicionados ----------------------------------------------------
        frame_tabela = ttk.LabelFrame(container, text=" Itens Adicionados ")
        frame_tabela.pack(fill="both", expand=True, padx=16, pady=(6, 6))

        colunas = ("produto", "quantidade", "subtotal")
        self.tabela = ttk.Treeview(
            frame_tabela, columns=colunas, show="headings", height=6
        )
        self.tabela.heading("produto", text="Produto")
        self.tabela.heading("quantidade", text="Quantidade")
        self.tabela.heading("subtotal", text="Subtotal")
        self.tabela.column("produto", width=280)
        self.tabela.column("quantidade", width=90, anchor="center")
        self.tabela.column("subtotal", width=110, anchor="e")
        self.tabela.pack(fill="both", expand=True, padx=10, pady=(8, 4))

        btn_remover = tk.Button(
            frame_tabela, text="Remover item selecionado", bg="#eb5757", fg="white",
            relief="flat", command=self._remover_item, padx=8, pady=4
        )
        btn_remover.pack(anchor="e", padx=10, pady=(0, 8))

        # --- Resumo Financeiro ----------------------------------------------------
        frame_resumo = ttk.LabelFrame(container, text=" Resumo Financeiro ")
        frame_resumo.pack(fill="x", padx=16, pady=(6, 12))

        self.lbl_total_bruto = self._linha_resumo(frame_resumo, "Total Bruto:")
        self.lbl_desconto = self._linha_resumo(frame_resumo, "Desconto Aplicado:", cor="#eb5757")
        ttk.Separator(frame_resumo).pack(fill="x", padx=10, pady=6)
        self.lbl_total_geral = self._linha_resumo(
            frame_resumo, "Total Geral:", tamanho=13, cor="#2f80ed", negrito=True
        )

        # --- Botão Salvar PDF ----------------------------------------------------
        btn_pdf = tk.Button(
            self, text="📄  Salvar Orçamento em PDF", bg="#27ae60", fg="white",
            relief="flat", font=("Segoe UI", 11, "bold"),
            command=self._salvar_pdf, pady=10
        )
        btn_pdf.pack(fill="x", padx=16, pady=(0, 16))

        self._atualizar_totais()

    def _linha_resumo(self, parent, texto, tamanho=11, cor="#1f2933", negrito=False):
        linha = ttk.Frame(parent)
        linha.pack(fill="x", padx=10, pady=3)
        fonte = ("Segoe UI", tamanho, "bold" if negrito else "normal")
        ttk.Label(linha, text=texto, font=fonte).pack(side="left")
        valor = tk.Label(linha, text=formatar_moeda(0), font=fonte, fg=cor)
        valor.pack(side="right")
        return valor

    # ------------------------------------------------------------------
    # LÓGICA
    # ------------------------------------------------------------------
    def _atualizar_produtos(self, event=None):
        grupo_selecionado = self.combo_grupo.get()

        produtos_grupo = [
            p for p in PRODUTOS
            if p["grupo"] == grupo_selecionado
        ]

        valores = [
            f"{p['codigo']} - {p['nome']} | {formatar_moeda(p['preco'])}"
            for p in produtos_grupo
        ]

        self.combo_produto["values"] = valores

        if valores:
            self.combo_produto.current(0)
        else:
            self.combo_produto.set("")

    def _adicionar_item(self):
        indice = self.combo_produto.current()
        if indice < 0:
            messagebox.showwarning("Atenção", "Selecione um produto.")
            return

        texto_qtd = self.entry_quantidade.get().strip().replace(",", ".")
        try:
            quantidade = float(texto_qtd)
            if quantidade <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Atenção", "Informe uma quantidade válida (maior que zero).")
            return

        grupo_selecionado = self.combo_grupo.get()

        produtos_grupo = [
            p for p in PRODUTOS
            if p["grupo"] == grupo_selecionado
        ]

        produto = produtos_grupo[indice]
        subtotal = produto["preco"] * quantidade

        self.itens.append({
            "codigo": produto["codigo"],
            "nome": produto["nome"],
            "preco": produto["preco"],
            "quantidade": quantidade,
            "subtotal": subtotal,
        })

        self.tabela.insert(
            "", "end",
            values=(
                f"{produto['codigo']} - {produto['nome']}",
                self._formatar_qtd(quantidade),
                formatar_moeda(subtotal),
            )
        )

        self.entry_quantidade.delete(0, tk.END)
        self.entry_quantidade.insert(0, "1")
        self._atualizar_totais()

    def _remover_item(self):
        selecionado = self.tabela.selection()
        if not selecionado:
            messagebox.showinfo("Info", "Selecione um item na tabela para remover.")
            return
        for item_id in selecionado:
            indice = self.tabela.index(item_id)
            self.tabela.delete(item_id)
            del self.itens[indice]
        self._atualizar_totais()

    @staticmethod
    def _formatar_qtd(qtd: float) -> str:
        return str(int(qtd)) if qtd == int(qtd) else f"{qtd:.2f}"

    def _atualizar_totais(self):
        total_bruto = sum(i["subtotal"] for i in self.itens)
        percentual_desconto = CONDICOES_DESCONTO.get(self.combo_desconto.get(), 0.0)
        desconto = total_bruto * (percentual_desconto / 100)
        total_geral = total_bruto - desconto

        self.lbl_total_bruto.config(text=formatar_moeda(total_bruto))
        self.lbl_desconto.config(text=f"- {formatar_moeda(desconto)}")
        self.lbl_total_geral.config(text=formatar_moeda(total_geral))

    # ------------------------------------------------------------------
    # PDF
    # ------------------------------------------------------------------
    def _salvar_pdf(self):
        if not self.itens:
            messagebox.showwarning("Atenção", "Adicione ao menos um item antes de salvar o orçamento.")
            return

        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.lib.units import cm
            from reportlab.pdfgen import canvas
        except ImportError:
            messagebox.showerror(
                "Biblioteca ausente",
                "Para exportar em PDF, instale a biblioteca reportlab:\n\npip install reportlab"
            )
            return

        cliente = self.entry_cliente.get().strip() or "Não informado"
        caminho = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("Arquivo PDF", "*.pdf")],
            initialfile=f"orcamento_{cliente.replace(' ', '_')}.pdf",
        )
        if not caminho:
            return

        total_bruto = sum(i["subtotal"] for i in self.itens)
        percentual_desconto = CONDICOES_DESCONTO.get(self.combo_desconto.get(), 0.0)
        desconto = total_bruto * (percentual_desconto / 100)
        total_geral = total_bruto - desconto

        c = canvas.Canvas(caminho, pagesize=A4)
        largura, altura = A4
        margem = 2 * cm
        y = altura - margem

        c.setFont("Helvetica-Bold", 16)
        c.drawString(margem, y, "Orçamento de Venda")
        y -= 0.9 * cm

        c.setFont("Helvetica", 10)
        c.drawString(margem, y, f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        y -= 0.6 * cm
        c.drawString(margem, y, f"Cliente: {cliente}")
        y -= 0.6 * cm
        c.drawString(margem, y, f"Tabela de Preço: {self.combo_tabela.get()}")
        y -= 0.6 * cm
        c.drawString(margem, y, f"Condição de Desconto: {self.combo_desconto.get()}")
        y -= 1.0 * cm

        c.setFont("Helvetica-Bold", 11)
        c.drawString(margem, y, "Produto")
        c.drawString(margem + 9 * cm, y, "Qtd")
        c.drawString(margem + 11.5 * cm, y, "Subtotal")
        y -= 0.3 * cm
        c.line(margem, y, largura - margem, y)
        y -= 0.5 * cm

        c.setFont("Helvetica", 10)
        for item in self.itens:
            if y < margem + 4 * cm:
                c.showPage()
                y = altura - margem
                c.setFont("Helvetica", 10)
            nome = f"{item['codigo']} - {item['nome']}"
            if len(nome) > 45:
                nome = nome[:42] + "..."
            c.drawString(margem, y, nome)
            c.drawString(margem + 9 * cm, y, self._formatar_qtd(item["quantidade"]))
            c.drawString(margem + 11.5 * cm, y, formatar_moeda(item["subtotal"]))
            y -= 0.55 * cm

        y -= 0.5 * cm
        c.line(margem, y, largura - margem, y)
        y -= 0.8 * cm

        c.setFont("Helvetica", 11)
        c.drawString(margem, y, "Total Bruto:")
        c.drawRightString(largura - margem, y, formatar_moeda(total_bruto))
        y -= 0.6 * cm
        c.drawString(margem, y, "Desconto Aplicado:")
        c.drawRightString(largura - margem, y, f"- {formatar_moeda(desconto)}")
        y -= 0.6 * cm
        c.setFont("Helvetica-Bold", 13)
        c.drawString(margem, y, "Total Geral:")
        c.drawRightString(largura - margem, y, formatar_moeda(total_geral))

        c.save()
        messagebox.showinfo("Sucesso", f"Orçamento salvo em:\n{caminho}")


if __name__ == "__main__":
    app = SimuladorVendas()
    app.mainloop()