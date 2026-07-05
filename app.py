import streamlit as st

from orchestrator import SQLSenseOrchestrator

st.set_page_config(page_title="SQLSense AI")

st.title("TextToSQL")
st.caption("Multi-Agent Text-to-SQL System")

question = st.text_input(
    "Ask your database anything..."
)

if st.button("Generate"):

    orchestrator = SQLSenseOrchestrator()

    context = orchestrator.run(question)

    st.success("Completed")

    st.subheader(" Intent")

    st.json(context.intent)

    st.subheader(" Selected Tables")

    st.json(context.selected_schema)

    st.subheader(" Generated SQL")

    st.code(context.validated_sql, language="sql")

    st.subheader(" Results")

    st.dataframe(context.results)

    st.subheader(" AI Analysis")

    st.write(context.analysis)

    st.subheader(" Agent Logs")

    for log in context.logs:

        st.write(
            f" {log['agent']} - {log['message']}"
        )