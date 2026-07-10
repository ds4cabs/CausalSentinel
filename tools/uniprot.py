"""
CausalSentinel · 工具:UniProt 蛋白档案查询 (get_uniprot_dossier)

改编自训练 repo:
  cabs-workshop-llm-agents/notebooks/02_gene_lookup_agent.ipynb 里的 lookup_gene_uniprot()

改了什么:
  1. 去掉 LangChain 的 @tool 装饰器 —— 因为本项目用 google-generativeai 的
     automatic function calling,普通函数(带类型注解 + docstring)就能当工具。
  2. 返回 dict 而不是字符串 —— 方便后面拼装 causal card 的 JSON。
  3. 加了 timeout 和 __main__ 测试块 —— 好单独测试(“先测工具,再交给 agent”)。

这是 MVP 里 8 个工具中的第 2 个。其余 7 个(Open Targets / ChEMBL / ClinVar /
gnomAD / GWAS Catalog / PharmGKB / OpenGWAS)是同一个套路:换 URL + 换解析字段。
"""

import requests

UNIPROT_SEARCH_URL = "https://rest.uniprot.org/uniprotkb/search"


def get_uniprot_dossier(protein: str) -> dict:
    """查询一个人类蛋白在 UniProt 里的档案。

    什么时候用:需要蛋白的功能(function)、亚细胞定位(location)、
    或疾病关联(disease)时。
    输入:标准基因符号,如 PNPLA3、TP53、HSD17B13。
    返回:包含 accession / 功能 / 定位 / 疾病 / 链接的 dict。
    """
    params = {
        # 只要人类(organism_id 9606)且经过人工审阅(reviewed)的高质量条目
        "query": f"(gene:{protein}) AND (organism_id:9606) AND (reviewed:true)",
        "format": "json",
        "size": 1,  # 只取最匹配的第一条
        "fields": "accession,gene_names,protein_name,cc_function,"
                  "cc_subcellular_location,cc_disease",
    }
    resp = requests.get(UNIPROT_SEARCH_URL, params=params, timeout=30)
    if resp.status_code != 200:
        return {"protein": protein, "error": f"UniProt API 返回状态码 {resp.status_code}"}

    results = resp.json().get("results", [])
    if not results:
        return {"protein": protein, "error": f"没找到 '{protein}' 的人类 reviewed 条目"}

    entry = results[0]
    accession = entry.get("primaryAccession", "N/A")

    # 蛋白全名
    protein_name = (
        entry.get("proteinDescription", {})
        .get("recommendedName", {})
        .get("fullName", {})
        .get("value", "N/A")
    )
    # 基因名(可能有多个别名)
    gene_names = [g.get("geneName", {}).get("value", "") for g in entry.get("genes", [])]

    # 从 comments 里挑出 功能 / 定位 / 疾病 三类注释
    functions, locations, diseases = [], [], []
    for c in entry.get("comments", []):
        ctype = c.get("commentType")
        if ctype == "FUNCTION":
            functions += [t.get("value", "") for t in c.get("texts", [])]
        elif ctype == "SUBCELLULAR LOCATION":
            locations += [
                loc.get("location", {}).get("value", "")
                for loc in c.get("subcellularLocations", [])
            ]
        elif ctype == "DISEASE":
            d = c.get("disease", {})
            if d:
                diseases.append(d.get("diseaseId", ""))

    return {
        "protein": protein,
        "accession": accession,
        "gene_names": [g for g in gene_names if g],
        "protein_name": protein_name,
        "function": " ".join(functions) or None,
        "subcellular_location": [l for l in locations if l],
        "diseases": [d for d in diseases if d],
        "url": f"https://www.uniprot.org/uniprotkb/{accession}",
    }


if __name__ == "__main__":
    # 单独测试这个工具:拿 MVP 里的真实靶点 PNPLA3(MASLD 相关)试一下
    import json
    dossier = get_uniprot_dossier("PNPLA3")
    print(json.dumps(dossier, indent=2, ensure_ascii=False))
