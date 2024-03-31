# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "They are not all mutually exclusive. For example, consider a person who is a Home Owner (Home Owner = Yes) and also has an Annual Income that is Low (Annual Income = Low). Both Rule 1 (Home Owner = Yes → DB = Yes) and Rule 3 (Annual Income = Low → DB = Yes) would apply to this person, indicating these rules are not mutually exclusive."
    answers["(b) explain"] = "The rule set is not entirely exhaustive because there are potential combinations of attribute values that are not explicitly addressed by the rules as they stand."
    answers["(c) explain"] = "Ordering is needed because the rules are not mutually exclusive, meaning a data point could potentially satisfy more than one rule. For example, if a person is a Home Owner and Single, both Rule 1 (Home Owner = Yes → DB = Yes) and Rule 2 (Marital Status = Single → DB = Yes) could apply."
    answers["(d) explain"] = "Since the rules are not exhaustive, there could be individuals for whom none of the provided rules apply directly. This scenario highlights the need for a default class."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) example"] = "The rules are not mutually exclusive because there are cases where an animal might satisfy conditions from multiple rules but belong to only one class."
    answers["(b) example"] = "The rules are not exhaustive because they do not account for all possible combinations of characteristics that can be observed in vertebrates."
    answers["(c) example"] = "Since the rules are not mutually exclusive, ordering is needed to prevent misclassification."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "The gradients of the weights at layer K+1 are computed using the chain rule, which relates these gradients to the gradients at layer k, effectively propagating the error information backward through the network to update the weights accordingly."
    answers["(b) explain"] = "The activations of nodes at the K+1th layer in an ANN are indeed computed using the activations of nodes at the Kth layer. This computation involves applying weights to the activations from the kth layer, adding biases, and then applying a non-linear activation function. This process allows the network to transform the input data layer by layer until the final output is produced."
    answers["(c) explain"] = "The vanishing gradient problem in ANN training refers to the issue where gradients become increasingly smaller as the error is backpropagated through the layers, making it difficult to update the weights in the earlier layers. This problem does not relate to training errors vanishing to zero while test errors remain large; that scenario is more indicative of overfitting."
    answers["(d) explain"] = "If an ANN model perfectly classifies all training instances, the loss function itself may reach a very low value, indicating that the model predictions are very close to the actual outcomes. However, this doesn't guarantee that the gradients of the loss with respect to the weights are zero."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "no"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = "+"
    answers["(d) Row 2"] = "-"
    answers["(d) Row 3"] = "-"
    answers["(d) Row 4"] = "-"

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.38 #doubt

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 5#5 doubt
    answers["(b) K"] = 5#doubt

    # explain_string
    answers["(a) explain"] = "Choosing K = 1 might overfit and choosing K=50 might cause underfit, so K=5 work well because each point would be classified according to its nearest 5 neighbors, and given the clear separation, it's unlikely to misclassify."
    answers["(b) explain"] = "K = 5 provides a balance by considering more neighbors which can reduce the effect of noise and outliers."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "There were 3 instances where A is 1 and the class is positive (Instances 2, 5, and 10), There were a total of 5 instances classified as positive. This means there's a 60% chance that A will be 1 in an instance that is classified as positive, based on the observed data."
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1.0
    answers["(b) P(R|+)"] = 0.2
    answers["(b) P(R|-)"] = 0.0

    # string, '+' or '-'
    answers["(b) class label"] = "+"

    # explain_string
    answers["(b) Explain your reasoning"] = "Using Naive Bayes, we calculate the likelihood of R given each class by multiplying the conditional probabilities of its features given the class. Since P(R|+) > P(R|-), R is more likely to belong to the positive class. This method assumes feature independence within each class."
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = "yes"
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = "yes"
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = "no"

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "A and B are not conditionally independent given class + because the joint probability P(A=1,B=1|+) does not equal the product of the individual probabilities P(A=1|+) and P(B=1|+). This indicates the occurrence of A being 1 is somewhat related to B being 1 within the subset of positive instances."
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
