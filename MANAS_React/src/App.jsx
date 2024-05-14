import { useState } from "react";
import axios from "axios";

// main.Main()

function App() {
  const [formData, setFormData] = useState({
    schizophrenia: "",
    bipolar: "",
    eating: "",
    anxiety: "",
    drugUse: "",
    depressive: "",
    alcoholUse: "",
    regressionMethod:"RandomForestRegressor"
  });

  const [responseData, setResponseData] = useState(null);
  const [selectedMethod, setSelectedMethod] = useState(
    "RandomForestRegressor"
  );

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    if (name === "regressionMethod") {
      setSelectedMethod(value);
    }
    setFormData({
      ...formData,
      [name]: value,
    });
  };


  const [loading, setLoading] = useState(false);
  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    try {
      const jsonData = JSON.stringify(formData);
      console.log(jsonData);
      const response = await axios.post(
        "http://localhost:5000/data/disorders",
        jsonData,
        {
          headers: {
            "Content-Type": "application/json",
          }
        }
      );

      setResponseData(response.data);
      console.log(responseData);
      console.log(selectedMethod);
    } catch (error) {
      console.error("Error:", error);
    } finally{
      setLoading(false);
    }
  };
  return (
    <div className="flex flex-col p-6 bg-white rounded-lg">
      <div className="flex flex-col w-full gap-[2rem]">
        <div className="flex flex-col w-full">
          <h2 className="text-[#5fb759] text-4xl mb-4 flex items-center text-center font-extrabold justify-center">
            IMPACT PREDICTOR
          </h2>
        </div>
        <div className="justify-center flex">
          <h1>
            Predicts the Disability-Adjusted Life Years (DALYs) impact of
            various mental health disorders based on prevalence parameter.
          </h1>
        </div>
        <form onSubmit={handleSubmit}>
          <div className="mb-4 flex items-center ">
            <label className="block text-gray-700 w-[30%] font-bold mb-2">
              {" "}
              Prevalence - Schizophrenia&nbsp;Disorders:
            </label>
            <input
              type="text"
              name="schizophrenia"
              value={formData.schizophrenia}
              onChange={handleInputChange}
              className="w-full border border-gray-300 p-2 rounded-md"
            />
          </div>
          <div className="mb-4 flex items-center">
            <label className="block text-gray-700 w-[30%] font-bold mb-2">
              {" "}
              Prevalence - Bipolar Disorders:
            </label>
            <input
              type="text"
              name="bipolar"
              value={formData.bipolar}
              onChange={handleInputChange}
              className="w-full border border-gray-300 p-2 rounded-md"
            />
          </div>
          <div className="mb-4 flex items-center">
            <label className="block text-gray-700 w-[30%] font-bold mb-2">
              {" "}
              Prevalence - Eating Disorders:
            </label>
            <input
              type="text"
              name="eating"
              value={formData.eating}
              onChange={handleInputChange}
              className="w-full border border-gray-300 p-2 rounded-md"
            />
          </div>
          <div className="mb-4 flex items-center">
            <label className="block text-gray-700 w-[30%]  font-bold mb-2">
              {" "}
              Prevalence - Anxiety Disorders:
            </label>
            <input
              type="text"
              name="anxiety"
              value={formData.anxiety}
              onChange={handleInputChange}
              className="w-full border border-gray-300 p-2 rounded-md"
            />
          </div>
          <div className="mb-4 flex items-center">
            <label className="block text-gray-700 w-[30%] font-bold mb-2">
              {" "}
              Prevalence - Drug Use Disorders:
            </label>
            <input
              type="text"
              name="drugUse"
              value={formData.drugUse}
              onChange={handleInputChange}
              className="w-full border border-gray-300 p-2 rounded-md"
            />
          </div>
          <div className="mb-4 flex items-center">
            <label className="block text-gray-700 w-[30%] font-bold mb-2">
              {" "}
              Prevalence - Depressive Disorders:
            </label>
            <input
              type="text"
              name="depressive"
              value={formData.depressive}
              onChange={handleInputChange}
              className="w-full border border-gray-300 p-2 rounded-md"
            />
          </div>
          <div className="mb-4 flex items-center">
            <label className="block text-gray-700 w-[30%] font-bold mb-2">
              {" "}
              Prevalence - Alcohol Use Disorders:
            </label>
            <input
              type="text"
              name="alcoholUse"
              value={formData.alcoholUse}
              onChange={handleInputChange}
              className="w-full border border-gray-300 p-2 rounded-md"
            />
          </div>
          <div className="flex mt-4 items-center">
            <label className="block text-gray-700 w-[30%] font-bold mb-2">
              Regression Method:
            </label>
            <select
              name="regressionMethod"
              value={formData.regressionMethod}
              onChange={handleInputChange}
              className="w-full border border-gray-300 p-2 rounded-md"
            >
              <option value="RandomForestRegressor">
                Random Forest Regression
              </option>
              <option value="BayesianRidge">
                Bayesian Regression
              </option>
              <option value="DecisionTreeRegressor">
                Decision Tree Regression
              </option>
              <option value="ElasticNet">
                Elastic Net Regression
              </option>
              <option value="GradientBoostingRegressor">
                Gradient Boosting Regression
              </option>
              <option value="KNeighborsRegressor">
                K-Nearest Neighbors Regression
              </option>
              <option value="Lasso">
                Lasso Regression
              </option>
              <option value="LinearRegressionr">
                Neural Network Regression
              </option>
              <option value="MLPRegressor">
                Polynomial Regression
              </option>
              <option value="Ridge">
                Ridge Regression
              </option>
              <option value="SVR">
                Support Vector Regression
              </option>
              <option value="XGBRegressor">
                XGBoost Regression
              </option>
            </select>
          </div>
          <button
            type="submit"
            className="mb-4 flex items-center justify-center w-full bg-[#5fb759] text-white font-bold py-2 px-4 rounded-md hover:bg-white hover:text-[#5fb759] border border-[#5fb759] transform-all duration-500"
          >
            {loading ? "Loading..." : "Predict"}
          </button>
        </form>
      </div>
      <div><h1></h1></div>
      <div className="flex justify-center w-full">
        {responseData && (
          <div className="mt-4 flex flex-col gap-5 justify-center items-center">
            <h3 className="text-gray-700 font-bold text-2xl mb-2">
              {responseData[selectedMethod] && (
                <tr key={selectedMethod} className="border">
                  Predicted DALYs : {responseData[selectedMethod].toFixed(2)}
                </tr>
              )}
            </h3>
          </div>
        )}
      </div>
      <div className="bg-[#eeecec] p-3 flex justify-center items-center">
          <h1 className="tracking-wide">
            Disclaimer: Above results are generated using machine learning
            models and should be interpreted with caution. They are intended for
            research purposes and may not represent real-world outcomes.
          </h1>
        </div>
      {/* <div>Here we are</div> */}
    </div>
  );
}

export default App;