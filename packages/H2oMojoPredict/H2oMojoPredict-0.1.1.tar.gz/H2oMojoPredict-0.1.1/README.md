# H2oMojoPredict 


### In H2oMojoPreidct, you can perform predictions on MOJO files without the need for H2O initialization or dependency on an H2O cluster. You are free to use Python to make predictions using MOJO files. 


## Running 
Follow these steps to set up and run :

### Prerequisites
- Python 3.7

### Installation

`pip install H2oMojoPredict`


Use demo :

    from H2oMojoPredict import H2oMojoPredicto
    # 初始化
    predictor = H2oMojoPredictor("XGBoost_model_python_1696751279647_2.zip", "binomial")
    # 输入数据格式
    data = pd.DataFrame({
            "os_act_first_diff": [55.0, 100.0],
            "life_cycle_string": ['4','3'],
        })
    # 启动java服务
    java_service = predictor.start_java_service()
    result = predictor.predict_with_java_service(java_service, data)
    print(result)`
    # 预测完毕，关闭java服务
    java_service.terminate()
    java_service.wait()
    if java_service.returncode == 0:
        print("Java service exited successfully.")
    else:
        print("Java service exited with an error code:", java_service.returncode)






