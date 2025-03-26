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




"""
def Classical_ML(st):
    st.header("Classical Machine Learning")
    st.subheader("Supervised Leanring")
    st.write(r" given {(x_i,y_i)| i=1,2,3,..n ; x_i \in R^d}")
    st.write("Learning from data: Loss ")
    st.write("Generizaton: Ideal  loss is Expected loss over all the samples  over the distribution. Key to split split training and test data. If we many models we need to select model. we split training  data  into training and validation. re train the whole model considering  train and validation and then test.")
    st.write("MLE maximize P(D|\theta) or P_{\theta)(D) | objective function")
    st.write("MAP maximize P(\theta|D) | objective function")

    st.write("prediction P_{\theta}(y|X=x) | Bayes rule  to naive bayes assumption")




    st.write("Knn --- Algorithm define S_x d(x,x^') <= d(x,x^'')")
    st.write("When #sample n tens to infinity then KNN will be twice the error rate of bayes optimal classifier ||When KNN will fail when thre is increase in dimention")
    
    st.write("Bayes Classifier: derivation, its the best classifier in the world.  ")


    st.write("Perceptron. convergence proof")
    


    st.write("1. from naive bayes rule to linear classification considering multinomial ")

    st.write("1. from naive bayes rule to logistic regression considering gaussion distrubion ")
    
    st.write("1. Consider Logistic regression formula and find params using MLE ")

    st.write("maximise usin MAP considering W is zero mean and sigma dist")


    st.write("find regression using MLE and MAP considering noiase as gaussian")

    st.write("linear support vector machine derivation, allow noise, kernel")

    st.write("Tree | impurity | derive entropy | split | random forest |CART")
    st.write("BAGGING using  generilation error| derive boosting ada-boost ")



    st.write("derive bias varience noise equation")
    st.write("Error vs regularizer| training error, test error bias varience, overfitting under fitting")
    st.write("Error vs  #iteration | training error, test error bias varience, overfitting under fitting")
    st.write("Error vs  #samples | training error, test error bias varience, overfitting under fitting| when to resolve  bagging boosting ")
   




    ######
    st.write("tranformer derivaition ")
    

    ##
    st.header("Liner Algebra")
    st.write("Ax  how to mulitiply| Column space , row spacei, rank | rank  1 matrix  "
    st.write("matrix factorization| A=LU ; A=QR  A=QVQ^T  ; SVD  "
    
    st.write("Eigen value and eigen vector| A^nx , M^-1AM ==B  similar, eigen values of Symmetric matrix are real and orthogonal  ")

    st.write("PSD and PD matrix and it properties| All the eigen values >0 ; x^TSA >0 for ll x!=0")
    st.write("S, T PD then S+T PD")


    st.write("derivaition  of SVD")

    


    ##deep learning
    1. regularization,Batch Norm , Layer Norm, drop out 
    2. RNN,LSTM,Transformer
    3. BERT, 

"""
    
 





 

    
    




def project_blue(st):
    st.header("Project Blue: Algorithmic Trading in the Indian Stock Market")
    st.write("""
    Project Blue is an ambitious initiative aimed at developing, backtesting, and deploying algorithmic trading strategies in the Indian stock market. 
    The project focuses on leveraging advanced data analysis, machine learning, and real-time market data to create robust trading systems.
    """)
    st.link_button("Project Blue", "https://github.com/ranjanZ/Blue")
    st.link_button("Project Blue: option chain analysis", "https://github.com/ranjanZ/Blue/blob/main/web/analysis_code/option_chain_v2.py")
    st.link_button("Project Blue: option and volume Divergence", "https://github.com/ranjanZ/Blue/tree/main/backtesting/backtest_options_v1/")
    st.link_button("Project Blue: All backtesting including  backtrade and backtesting.py ", "https://github.com/ranjanZ/Blue/tree/main/backtesting/backtest_index/analysis/bt")


   
    st.subheader("🚀 Project Timeline and Achievements")
    st.write("""
    Project Blue is a continuous journey with no end. It evolves as new challenges and opportunities arise in the market. 
    Below is the timeline of what has been accomplished so far and the roadmap for the future.
    """)

    # Timeline with Icons and Catchy Headlines
    st.write("### 📅 2023: Laying the Foundation")
    st.write("""
    - **📊 Understanding Equity, Futures, and Options**: 
      Gained a deep understanding of how equity, futures, and options behave in the Indian stock market.
    - **📈 Live Data Extraction and Visualization**: 
      Mastered live data extraction and visualization using libraries like Matplotlib, Dash, and Plotly.
    - **⚙️ Threading and Library Migration**: 
      Implemented threading for efficient data processing and transitioned between libraries for better performance.
    """)

    st.write("### 🛠️ 2024: Building the Tools")
    st.write("""
    - **🔧 Custom Library for Option Chain Analysis**: 
      Developed a proprietary library for analyzing option chains, focusing on volume spread analysis and IV (Implied Volatility) anomalies in intraday trading.
    - **📉 Volume Spread Analysis**: 
      Explored volume spread analysis to identify potential market movements and hidden trends.
    - **📊 IV Anomaly Detection**: 
      Built tools to detect IV anomalies in real-time for intraday trading opportunities.
    """)


    # Vertical Timeline with Circles and Lines
    st.write("### 2025 Timeline")

    # Define the timeline data
    milestones = [
        {"date": "January 2025", "description": "Explored Backtrader for strategy backtesting and optimization."},
        {"date": "February 2025", "description": "Integrated Backtrader with Fyers API for live trading."},
        {"date": "March 2025", "description": "Implemented live data fetching using TimeScaleDB. data fetching is saperate process done by time scale db. need tt run the process from cerebro. Intregrate historical Option data manement, storing effieciently weekly and monthly expiry data. ploty,dash for live data  and orders visulization,data sharing by redishserver over the process.separate process for visualization so that it does not efect the strategy computation.indicator intregration will be done later" }, 
        {"date": "April 2025", "description": "Backtesting and finding Alpha, Target: low drawdown target  sharpe ratio  of >2. Use option Selling methods"},
        {"date": "May 2025", "description": "Kedernath Jatra: deploy on paper trading, ingtregate live order"},

    ]


    # Create a vertical timeline
    for i, milestone in enumerate(milestones):
        # Create columns for the timeline
        col1, col2, col3 = st.columns([0.01, 1, 8])  # Adjusted column widths for left alignment

        # Circle (Unicode character)
        with col1:
            st.write("")  # Empty space for alignment

        with col2:
            st.markdown(f"<div style='text-align: center; font-size: 24px;'>●</div>", unsafe_allow_html=True)

        # Milestone description (larger text)
        with col3:
            st.markdown(f"<div style='font-size: 18px;'><b>{milestone['date']}</b></div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size: 16px;'>{milestone['description']}</div>", unsafe_allow_html=True)

        # Add a vertical line between milestones (Unicode character)
        if i < len(milestones) - 1:
            col1, col2, col3 = st.columns([0.01, 1, 8])
            with col1:
                st.write("")  # Empty space for alignment
            with col2:
                st.markdown("<div style='text-align: center; font-size: 24px;'>│</div>", unsafe_allow_html=True)
            with col3:
                st.write(" ")  # Empty space for alignment





