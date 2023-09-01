import datetime

def set_dates_range(st):
    date_range = st.date_input(
        "Selete you date range",
        (datetime.datetime.now().replace(day=1), datetime.datetime.now()),
        format="MM.DD.YYYY",
    )
    if date_range:
        start_date = date_range[0]
        end_date   = date_range[1] if len(date_range) > 1 else date_range[0]
    return start_date , end_date



def set_two_inputs_date(st):
    col1, col2 = st.columns(2)

    with col1 :
        start_date = st.date_input("Select start date:")

    with col2:
        end_date = st.date_input("Select end date:")

    if start_date or end_date :
        return start_date , end_date
    
    