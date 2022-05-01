from rouge import Rouge  
from model import Summary
import numpy as np

def accuracyScores(sumOut,reference_text):

    hypothesis = sumOut

    reference = reference_text

    roug = Rouge()
    scores = roug.get_scores(hypothesis, reference)
    score_1 = round(scores[0]['rouge-1']['f'], 2)    
    score_2 = round(scores[0]['rouge-2']['f'], 2)    
    score_L = round(scores[0]['rouge-l']['f'], 2)

    print("rouge1:", score_1, "| rouge2:", score_2, "| rougeL:",
         score_2, "--> avg rouge:", round(np.mean(
         [score_1,score_2,score_L]), 2))

input_text = "there are two ways to become wealthy: to create wealth or to take wealth away from others. The former adds to society. The latter typically subtracts from it, for in the process of taking it away, wealth gets destroyed. A monopolist who overcharges for his product takes away money from those whom he is overcharging and at the same time destroys value. To get his monopaly price, he has to restrict production. Stiglitz, J.E. (2013). The price of inequality. London: Penguin."

sumObj = Summary()
summary = sumObj.summary(input_text)
referenceSum = "Stiglitz (2013) suggests that creating wealth adds value to society, but that taking away the wealth of others detracts from it. He uses the example of a monopolist who overcharges for his product resulting in loss of wealth for the customer, but also loss of value as the monapalist has to restrict production in order to charge the higher price"
print(accuracyScores(summary,referenceSum))