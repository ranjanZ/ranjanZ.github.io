import datetime
import calendar

def days_to_last_thursday(year, month):
    # Get the last day of the month
    last_day = datetime.date(year, month, calendar.monthrange(year, month)[1])
    
    # Find the last Thursday
    while last_day.weekday() != 3:  # 3 represents Thursday in Python's datetime
        last_day -= datetime.timedelta(days=1)
    
    #print("***", last_thursday, last_day)
    
    # Calculate the number of days between today and the last Thursday
    x = (last_day - datetime.date.today()).days
    
    return x


def compute_future_price(st):
    st.write("**Future Price Calculator**")

    # Input fields
        # Create columns for input fields
    col1, col2 = st.columns(2)

    # Input fields
    with col1:
        spot_price = st.number_input("Spot Price:")

    with col2:
        current_month = datetime.datetime.now().month
        month_options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        month_input = st.selectbox("Month:", month_options[current_month - 1:])

    # Risk-free rate input with default value
    #r = st.number_input("Risk-Free Rate (%)", width=100, value=7.0)  # Default value of 7%
    r = 0.07  # Fixed risk-free rate of 7%



    # Determine the last Thursday of the selected month
    year = datetime.date.today().year
    month_num = datetime.datetime.strptime(month_input, "%B").month
    x=days_to_last_thursday(year,month_num)

    
    # Calculate future price using the formula
    future_price = spot_price * (1 + r * x / 365)

    # Display the result
    if spot_price and month_input:
        st.write("**Future Price:**", future_price)



