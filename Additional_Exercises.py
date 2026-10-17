# ==========================================================
# APPENDIX: ADDITIONAL EXERCISES
# Student: Mark Vincent Viana | ID: TUPM-26-1953
# LAST_NAME: VIANA | SEED_NUM: 3 | FAVORITE_ARTIST: D4VD
# Char Positions: D=0, 4=1, V=2, D=3
# ==========================================================

SEED_NUM = 3
LAST_NAME = "VIANA"
FAVORITE_ARTIST = "D4VD"
# Positions: index 0='D', 1='4', 2='V', 3='D'

# ==========================================================
# MISSION 1: ENGINEERING TEST DATA ORGANIZER
# ==========================================================
print("="*70)
print("MISSION 1: ENGINEERING TEST DATA ORGANIZER")
print("="*70)

test_sources = {f"T{i+1}": LAST_NAME[i] for i in range(5)}
categories = ["TEMPERATURE", "PRESSURE", "VOLTAGE", "CURRENT", "SPEED"]

raw_records = [
    {"source": "T1", "category": "TEMPERATURE", "value": SEED_NUM + 10},
    {"source": "T2", "category": "PRESSURE",    "value": SEED_NUM + 11},
    {"source": "T3", "category": "VOLTAGE",     "value": SEED_NUM + 12},
    {"source": "T4", "category": "CURRENT",     "value": SEED_NUM + 13},
    {"source": "T5", "category": "SPEED",       "value": SEED_NUM + 14},
    {"source": "T1", "category": "TEMPERATURE", "value": SEED_NUM + 10},
    {"source": "T2", "category": "VOLTAGE",     "value": SEED_NUM + 12},
]

print("\n--- 1. GENERATED TEST DATA ---")
for rec in raw_records:
    print(f"  {rec['source']:4} | {rec['category']:12} | {rec['value']}")

organized = {}
for rec in raw_records:
    key = (rec["source"], rec["category"])
    organized[key] = rec["value"]

print("\n--- 2. ORGANIZED TEST DATA ---")
for (src, cat), val in organized.items():
    print(f"  {src:4} | {cat:12} | {val}")

seen, repeated, distinct = [], [], []
for rec in raw_records:
    key = (rec["source"], rec["category"])
    if key in seen:
        repeated.append(key)
    else:
        seen.append(key)
        distinct.append(rec)

print("\n--- 3. REPEATED / DISTINCT DATA ---")
print(f"  Repeated Entries: {len(repeated)} → {repeated if repeated else 'None'}")
print(f"  Distinct Records: {len(distinct)}")

source_totals = {}
cat_totals = {}
for rec in distinct:
    s, c, v = rec["source"], rec["category"], rec["value"]
    source_totals[s] = source_totals.get(s, 0) + v
    cat_totals[c] = cat_totals.get(c, 0) + v

print("\n--- 4. NUMERICAL SUMMARIES ---")
print("  By Source:")
for s, total in source_totals.items():
    print(f"    {s}: {total}")
print("  By Category:")
for c, total in cat_totals.items():
    print(f"    {c}: {total}")

ordered = sorted(distinct, key=lambda x: (x["source"], x["category"]))
print("\n--- 5. ORDERED RESULTS ---")
for rec in ordered:
    print(f"  {rec['source']:4} | {rec['category']:12} | {rec['value']}")

print("\n--- 6. FINAL SUMMARY ---")
print(f"  Total Records Processed: {len(raw_records)}")
print(f"  Unique Records Stored:   {len(distinct)}")
print(f"  Duplicates Removed:      {len(raw_records) - len(distinct)}")

# ==========================================================
# MISSION 2: STUDENT PERFORMANCE DATA ANALYZER
# ==========================================================
print("\n" + "="*70)
print("MISSION 2: STUDENT PERFORMANCE DATA ANALYZER")
print("="*70)

student_labels = [f"{LAST_NAME}_{c}" for c in ["S1", "S2", "S3", "S4", "S5"]]
subjects = ["PROGRAMMING", "MATHEMATICS", "ELECTRONICS", "PHYSICS", "ENGLISH"]

# Scores using D4VD positions: D=0, 4=1, V=2, D=3
performance_records = [
    {"student": student_labels[0], "subject": "PROGRAMMING", "score": SEED_NUM + 85 + 0},
    {"student": student_labels[1], "subject": "MATHEMATICS", "score": SEED_NUM + 82 + 1},
    {"student": student_labels[2], "subject": "ELECTRONICS", "score": SEED_NUM + 88 + 2},
    {"student": student_labels[3], "subject": "PHYSICS",     "score": SEED_NUM + 79 + 3},
    {"student": student_labels[4], "subject": "ENGLISH",     "score": SEED_NUM + 90 + 0},
    {"student": student_labels[0], "subject": "PROGRAMMING", "score": SEED_NUM + 85 + 0},
    {"student": student_labels[1], "subject": "PHYSICS",     "score": None},
]

print("\n--- 1. GENERATED PERFORMANCE RECORDS ---")
for rec in performance_records:
    sc = rec["score"] if rec["score"] is not None else "MISSING"
    print(f"  {rec['student']:15} | {rec['subject']:12} | {sc}")

student_data = {}
for rec in performance_records:
    s = rec["student"]
    if s not in student_data:
        student_data[s] = {}
    student_data[s][rec["subject"]] = rec["score"]

print("\n--- 2. ORGANIZED STUDENT DATA ---")
for student, subs in student_data.items():
    print(f"  {student}: {subs}")

seen_pairs, repeated_pairs, incomplete = [], [], []
for rec in performance_records:
    key = (rec["student"], rec["subject"])
    if rec["score"] is None:
        incomplete.append(key)
    elif key in seen_pairs:
        repeated_pairs.append(key)
    else:
        seen_pairs.append(key)

print("\n--- 3. REPEATED / INCOMPLETE RECORDS ---")
print(f"  Repeated:   {repeated_pairs if repeated_pairs else 'None'}")
print(f"  Incomplete: {incomplete if incomplete else 'None'}")

def get_category(score):
    if score is None: return "INCOMPLETE"
    if score >= 90: return "OUTSTANDING"
    if score >= 80: return "SATISFACTORY"
    if score >= 75: return "FAIR"
    return "BELOW AVERAGE"

print("\n--- 4. PERFORMANCE CATEGORIES ---")
for rec in performance_records:
    cat = get_category(rec["score"])
    print(f"  {rec['student']:15} | {rec['subject']:12} | {cat}")

print("\n--- 5. STUDENT SUMMARIES ---")
for student in student_labels:
    scores = [v for v in student_data[student].values() if v is not None]
    if scores:
        avg = sum(scores) / len(scores)
        print(f"  {student}: Average = {avg:.2f}")
    else:
        print(f"  {student}: No valid scores")

print("\n--- 6. ORDERED RESULTS ---")
ordered_students = sorted(performance_records, key=lambda x: (x["student"], x["subject"]))
for rec in ordered_students:
    sc = rec["score"] if rec["score"] is not None else "MISSING"
    cat = get_category(rec["score"])
    print(f"  {rec['student']:15} | {rec['subject']:12} | {str(sc):>6} | {cat}")

print("\n--- 7. FINAL PERFORMANCE REPORT ---")
valid_scores = [r["score"] for r in performance_records if r["score"] is not None]
print(f"  Total Records: {len(performance_records)}")
print(f"  Valid Scores:  {len(valid_scores)}")
print(f"  Missing Data:  {len(incomplete)}")
if valid_scores:
    print(f"  Overall Avg:   {sum(valid_scores)/len(valid_scores):.2f}")

# ==========================================================
# MISSION 3: TRANSACTION HISTORY ANALYZER
# ==========================================================
print("\n" + "="*70)
print("MISSION 3: TRANSACTION HISTORY ANALYZER")
print("="*70)

customers = [f"{LAST_NAME}_{c}" for c in ["C1", "C2", "C3", "C4", "C5"]]
products = ["NOTEBOOK", "PEN", "USB", "HEADPHONES", "CALCULATOR"]
prices = {"NOTEBOOK": 45.0, "PEN": 12.0, "USB": 25.0, "HEADPHONES": 120.0, "CALCULATOR": 65.0}

# Quantities using D4VD positions: D=0, 4=1, V=2, D=3
transactions = [
    {"customer": customers[0], "product": "NOTEBOOK",     "qty": SEED_NUM + 0},
    {"customer": customers[1], "product": "PEN",          "qty": SEED_NUM + 1},
    {"customer": customers[2], "product": "USB",          "qty": SEED_NUM + 2},
    {"customer": customers[3], "product": "HEADPHONES",   "qty": SEED_NUM + 3},
    {"customer": customers[4], "product": "CALCULATOR",   "qty": SEED_NUM + 0},
    {"customer": customers[0], "product": "NOTEBOOK",     "qty": SEED_NUM + 0},
    {"customer": customers[1], "product": "USB",          "qty": SEED_NUM + 1},
]

for t in transactions:
    t["amount"] = t["qty"] * prices[t["product"]]

print("\n--- 1. GENERATED TRANSACTION RECORDS ---")
for t in transactions:
    print(f"  {t['customer']:12} | {t['product']:12} | Qty: {t['qty']:2} | Amount: ₱{t['amount']:.2f}")

seen_tx, repeated_tx = [], []
for t in transactions:
    key = (t["customer"], t["product"], t["qty"])
    if key in seen_tx:
        repeated_tx.append(key)
    else:
        seen_tx.append(key)

print("\n--- 2. REPEATED TRANSACTIONS ---")
print(f"  Repeated: {repeated_tx if repeated_tx else 'None'}")

by_customer = {}
by_product = {}
for t in transactions:
    c, p = t["customer"], t["product"]
    by_customer.setdefault(c, []).append(t)
    by_product.setdefault(p, []).append(t)

print("\n--- 3. CUSTOMER SUMMARIES ---")
for cust in customers:
    tx_list = by_customer.get(cust, [])
    total = sum(t["amount"] for t in tx_list)
    print(f"  {cust:12} | Total Spent: ₱{total:.2f}")

print("\n--- 4. PRODUCT SUMMARIES ---")
for prod in products:
    qty_total = sum(t["qty"] for t in transactions if t["product"] == prod)
    sales_total = sum(t["amount"] for t in transactions if t["product"] == prod)
    print(f"  {prod:12} | Sold: {qty_total:2} | Sales: ₱{sales_total:.2f}")

print("\n--- 5. ORDERED TRANSACTIONS ---")
ordered_tx = sorted(seen_tx, key=lambda x: (x[0], -(x[2] * prices[x[1]])))
for c, p, qty in ordered_tx:
    amt = qty * prices[p]
    print(f"  {c:12} | {p:12} | Qty: {qty:2} | Amount: ₱{amt:.2f}")

print("\n--- 6. OVERALL TRANSACTION SUMMARY ---")
total_sales_all = sum(t["amount"] for t in transactions)
unique_sales = sum(qty * prices[p] for c, p, qty in seen_tx)
print(f"  Total Transactions: {len(transactions)}")
print(f"  Unique Transactions: {len(seen_tx)}")
print(f"  Duplicates Found:    {len(repeated_tx)}")
print(f"  Total Sales (Gross): ₱{total_sales_all:.2f}")
print(f"  Unique Sales Value:  ₱{unique_sales:.2f}")

print("\n" + "="*70)
print("APPENDIX COMPLETE")
print("="*70)