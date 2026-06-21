import streamlit as st

st.title("MSME Navigator AI")

st.write("A Multi-Agent Business Consulting System for MSMEs")

industry = st.text_input("Industry")
revenue = st.number_input("Annual Revenue (₹)", min_value=0)
employees = st.number_input("Number of Employees", min_value=1)
challenge = st.text_area("Describe your business challenge")

if st.button("Analyze Business"):

    st.subheader("Financial Agent")
    st.write("Potential working capital and cash flow considerations identified.")

    st.subheader("Credit Agent")
    st.write("Business may explore suitable financing and credit options.")

    st.subheader("Growth Agent")
    st.write("Potential opportunities for expansion, customer acquisition, and operational improvement.")

    st.subheader("Government Scheme Agent")
    st.write("Relevant MSME schemes and support programs may be applicable.")

    st.subheader("Consultant Agent")
    st.write(
        f"""
        Business Summary:
        Industry: {industry}

        Revenue: ₹{revenue}

        Employees: {employees}

        Challenge: {challenge}

        Recommended next step:
        Conduct detailed financial review and prioritize growth initiatives.
        """
    )
