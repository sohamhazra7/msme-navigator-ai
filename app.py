import streamlit as st

st.title("MSME Navigator AI")
st.write("A Multi-Agent Business Consulting System for MSMEs")

industry = st.text_input("Industry")
revenue = st.number_input("Annual Revenue (₹)", min_value=0)
employees = st.number_input("Number of Employees", min_value=1)
challenge = st.text_area("Describe your business challenge")

if st.button("Analyze Business"):

    # Financial Agent
    st.header("Financial Agent")

    if revenue < 1000000:
        st.write(
            "The business appears to operate at a relatively small scale. Improving cash flow visibility, budgeting practices, and working capital management should be prioritized."
        )
    elif revenue < 10000000:
        st.write(
            "The business has growth potential but should strengthen financial planning, receivables management, and profitability monitoring."
        )
    else:
        st.write(
            "The business demonstrates significant scale. Focus should be on financial efficiency, capital allocation, and sustainable growth."
        )

    # Credit Agent
    st.header("Credit Agent")

    if (
        "loan" in challenge.lower()
        or "credit" in challenge.lower()
        or "finance" in challenge.lower()
        or "financing" in challenge.lower()
    ):
        st.write(
            "The challenge suggests financing constraints. The business should improve financial documentation, maintain credit discipline, and explore MSME financing options."
        )
    elif "cash flow" in challenge.lower():
        st.write(
            "Cash flow concerns indicate a need for better receivables management and working capital financing solutions."
        )
    else:
        st.write(
            "The business should periodically assess its credit readiness and maintain strong financial records."
        )

    # Growth Agent
    st.header("Growth Agent")

    if employees < 20:
        st.write(
            "The business may benefit from expanding its customer base, strengthening its digital presence, and improving operational efficiency."
        )
    else:
        st.write(
            "The business has workforce capacity to pursue market expansion, product diversification, and process optimization."
        )

    # Government Scheme Agent
    st.header("Government Scheme Agent")

    st.write(
        "The business may explore MSME-focused government initiatives, credit guarantee schemes, and entrepreneurship support programs based on eligibility."
    )

    # Consultant Agent
    st.header("Consultant Agent")

    st.subheader("Business Summary")

    st.write(f"Industry: {industry}")
    st.write(f"Annual Revenue: ₹{revenue:,.0f}")
    st.write(f"Employees: {employees}")
    st.write(f"Challenge: {challenge}")

    st.subheader("Recommended Action Plan")

    if "cash flow" in challenge.lower():
        st.write("• Improve cash flow forecasting and working capital management.")

    if (
        "loan" in challenge.lower()
        or "credit" in challenge.lower()
        or "finance" in challenge.lower()
        or "financing" in challenge.lower()
    ):
        st.write("• Strengthen credit profile and explore financing alternatives.")

    if (
        "growth" in challenge.lower()
        or "expansion" in challenge.lower()
    ):
        st.write("• Develop a structured growth and market expansion strategy.")

    st.write(
        "• Conduct periodic financial reviews and track key business performance indicators."
    )
