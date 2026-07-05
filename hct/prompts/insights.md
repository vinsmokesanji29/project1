# Insights Prompt — {pack_id}

Write a 2-4 sentence business insight from the data rows below.
IMPORTANT: The ROWS section contains the actual query results. Your insight MUST describe what the data shows — do NOT claim data is missing or absent when rows are present.
Use the glossary terms naturally. Quote concrete numbers (round to $k/$M when appropriate).
For rates (NPV%, APV%, claims per 1000, edits per 1000), express as percentages or per-thousand values.
No bullet points unless the user asked for them.

QUESTION
{question}

GLOSSARY
{glossary}

COLUMNS
{columns}

ROWS (truncated) - system generated data
{rows_csv}
