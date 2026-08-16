# Developed healthcare recommendations based on detected risk factors of the patients and their health conditions.
# Handled function, generate_recommendations, and get_recommendations, to generate and return appropriate care recommendations.



# Creating health recommendations
def generate_recommendations(factors):


    # Creating recommendation list
    recommendations = []



    # Checking patient risk factors
    for factor in factors:



        # Checking blood pressure risk
        if factor == "High Blood Pressure":


            # Adding blood pressure guidance
            recommendations.append(

                "Monitor blood pressure regularly"

            )


            # Adding diet guidance
            recommendations.append(

                "Reduce sodium intake"

            )



        # Checking blood sugar risk
        elif factor == "High Blood Sugar":


            # Adding glucose monitoring guidance
            recommendations.append(

                "Perform glucose monitoring"

            )


            # Adding diabetes care guidance
            recommendations.append(

                "Maintain diabetic care plan"

            )



        # Checking smoking risk
        elif factor == "Smoking History":


            # Adding smoking guidance
            recommendations.append(

                "Consider smoking cessation program"

            )



        # Checking BMI risk
        elif factor == "High BMI":


            # Adding fitness guidance
            recommendations.append(

                "Follow healthy diet and exercise plan"

            )



        # Checking oxygen risk
        elif factor == "Low Oxygen Level":


            # Adding respiratory guidance
            recommendations.append(

                "Evaluate respiratory condition"

            )



        # Checking age risk
        elif factor == "Advanced Age":


            # Adding checkup guidance
            recommendations.append(

                "Schedule regular healthcare checkups"

            )



    # Checking recommendation availability
    if len(recommendations) == 0:


        # Adding healthy lifestyle guidance
        recommendations.append(

            "Continue current healthy lifestyle"

        )



    # Returning recommendation list
    return recommendations





# Providing recommendation API function
def get_recommendations(factors):


    # Returning generated recommendations
    return generate_recommendations(factors)