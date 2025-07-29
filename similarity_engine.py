from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_similarity(jd_text, resumes, resume_names):
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)
    resume_embeddings = model.encode(resumes, convert_to_tensor=True)

    cosine_scores = util.pytorch_cos_sim(jd_embedding, resume_embeddings)[0]
    results = []

    for i, score in enumerate(cosine_scores):
        results.append((resume_names[i], float(score)))

    ranked = sorted(results, key=lambda x: x[1], reverse=True)
    return ranked
