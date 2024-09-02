from utils import *


base_path="https://raw.githubusercontent.com/ranjanZ/ranjanZ.github.io/master/streamlit_page/"

def blog_tensor_diff(st):
    st.write("""
    Before going into Deep learning, one of the major concepts is needed tensor calculus. To be more specific we need to know how to differentiate a scaler/vector/matrix with respect to vector/matrix. In this blog I am going discuss that will be needed in to understand Deep learning.

    """)
    st.write("""
    Differentiation of scalar with respect to vector/Matrix
    """)

    st.latex(r""" \frac{\partial f(\X)}{\partial \X} = \begin{bmatrix} \frac{\partial f(\X)}{\partial x_1} \\ \frac{\partial f(\X)}{\partial x_2} \\ ..\\ .. \\ \frac{\partial f(\X)}{\partial x_n} \end{bmatrix}""")

    st.write(""" Note: Similarly when you do derivative of a scalar with respect to matrix the output will always be a matrix as the size of the matrix by which you are doing derivative. """)







def VSA(st):
    # content of the blogs page
    #st.title("Basics of Traiding and Financial Market")
    #st.latex(r""" \sum_{k=0}^{n-1} \pi e^{k}""")
    # Set the page background color
    st.markdown("""
        <style>
        .css-18e3th9 {
            background-color: #f0f2f6;
        }
        </style>
    """, unsafe_allow_html=True)

    # Create a title
    st.title("Volume Spread Analysis: A Powerful Tool for Market Insights")

    # Create a subheading
    st.subheader("Introduction")

    # Create a markdown section
    st.markdown("""
    Volume Spread Analysis (VSA) is a technical analysis technique used to identify market trends and patterns by analyzing the relationship between volume and price movements. VSA is based on the idea that volume precedes price movement, and by analyzing volume, traders can gain valuable insights into market sentiment and potential price movements.
    """)

    # Create a subheading
    st.subheader("Key Concepts of VSA")

    # Create a markdown section
    st.markdown("""
    * **Volume**: The amount of trading activity in a given period.
    * **Spread**: The difference between the high and low prices of a trading period.
    """)

    st.subheader("All Cases of VSA")
    st.write(r"""When I say High or Low, it's relative to other candles. Generally, the spread ($S$) is proportional to Volume ($V$), i.e., $S \propto kV$, where $k$ is a constant.
When we observe either $S$ or $V$ deviating from their normal range, it indicates an anomaly. Note that $S$ and $V$ are compared to their historical values to determine if they are relatively high or low.
""")
    st.markdown("""
    * **High Volume, High Spread**
    * **High Volume, Low Spread**
    * **Low Volume, High Spread**
    * **Low Volume, Low Spread**
    """)




    # Create a markdown section

    st.subheader("**High Volume High Spread**")
    st.image("./data/vsa/HVHS.png", caption="High Volume High Spread",width=800)
    st.markdown("---")

    st.subheader("**High Volume Low Spread**")
    st.image("./data/vsa/HVLS.png", caption="High Volume Low Spread",width=800)
    st.markdown("---")

    st.subheader("**Low Volume High Spread**")
    st.image("./data/vsa/LVHS.png", caption="Low Volume High Spread",width=800)
    st.markdown("---")

    st.subheader("**Low Volume Low Spread**")
    st.image("./data/vsa/LVLS.png", caption="Low Volume Low Spread",width=800)
    st.markdown("---")
    st.markdown("---")

    # Create a subheading
    st.header("How to Apply VSA")
    st.write("""
    - Low Volume: The smart money has no interest in the upside.
    - Higher Volume: Smart money is selling into the public buying.
    """)

    st.subheader("**High Spread with different Volume**")


    st.image("data/vsa/VHS.png", caption="High Spread with different Volume",width=800)
    st.markdown("---")



    st.subheader("**Narrow Spread with different Volume**")
    st.image("data/vsa/VLS.png", caption="Narrow Spread with different Volume",width=800)
    st.markdown("---")


    st.subheader("**Rejection candle with different volume**")
    st.image("data/vsa/VLS2.png", caption="Narrow Spread rejection with different volume",width=800)
    st.markdown("---")

    # Create a markdown section
    st.header("**Aplications**")
    st.markdown("""
    * **Early Warning System**: VSA can alert traders to potential price movements before they occur.
    * **Market Sentiment Insights**: VSA provides valuable insights into market sentiment and trader behavior.
    * **Improved Trading Decisions**: By analyzing volume and price movements, traders can make more informed trading decisions.
    """)
    st.markdown("---")

    st.subheader("**Statistical Analysis and Signal Generation:**")




def Arbitrage(st):
    st.header("Option and Future Pricing")
    st.subheader("Future Pricing")
    st.write("Futute price(F) depends on sport price(S)")
    st.write("The relation is as follows:")
    st.latex(r"F=S(1+R)-d=S(1+rx/365)-d")
    st.write("r is annual rate of risk free interest rate. x is number of days untill expiry. d is divident ")
    st.write("Lets not consider divident and make it simple as follows: ")
    st.latex(r"F=S(1+rx/365)")

    compute_future_price(st)


    st.subheader("Arbitrage in Future  vs spot")
    st.write("We track |futute - spot| ideally it should be zero or hover around zero.  you can see the distribution bellow taken from bank nifty  Future vs spot ")
    st.image(base_path + "data/fut_arbitrage.png",width=600)  # Replace with your image path
    st.write("when the parity value is far away from zero we can get grofit from it")

    st.write("Example: spot price 1628.65  fut 1633.45 parity is 2.696252(theoritical fut val - actual fut value), so fut is undervalues.  we can  buy fut  and sell spot.in some time it will be near diff will be near to zero, so we will close the position")
    st.write("total profit: 2.62*lotsize=2.62*550=1441.0, total capital needd = 176240*2=352480, brokerage=₹1,690.42*2~3000. we have to check where we can excceed the brokerage")









