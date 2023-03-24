class Student(object):
  # represents a student

  def __init__(self, name, number):
    # creates a student with the given name
    # and number of scores
    self.name = name
    self.number = number
    self.scores = []

    # initialize all scores to zero
    for i in range(number):
      self.scores.append(0)

  def getName(self):
    # returns the students name
    return self.name

  def getScore(self, i):
    # returns score with an index of i
    return self.scores[i]

  def __str__(self):
    # returns the string representation of the student's information

    index = 0 # index of score
    scoresString = "" # string of all scores

    # loop through scores
    for score in self.scores:
      # add the index and the value
      scoresString += "{0}:\t{1}\n".format(index, score)
      index += 1 # increment index

    # return all information
    return "Name: {0}\n# of scores: {1}\nscores:\n{2}".format(self.name, self.number, scoresString)

  def setScore(self, i, score):
    # set score with an index of i to the value of score
    self.scores[i] = score

  def setName(self, name):
    # change the student's name
    self.name = str(name)

  def getAverage(self):
    # returns the average of all the student's scores
    sum = 0 # sum of the scores

    # loop through scores to get the sum
    for score in self.scores:
      sum += score

    return sum / len(self.scores) # return avg

  def getHighScore(self):
    # return the student's highest score
    return max(self.scores)

  def greaterThan(self, other):
    # return a value of True if the average of self is greater
    # than or equal to the average of other; else return False

    if self.getAverage() >= other.getAverage(): # compare averages
        return True
    else:
        return False

  def equal(self, other):
    # return True if the average of self is equal to the
    # average of other; else return False

    if self.getAverage() == other.getAverage(): # compare averages
        return True
    else:
        return False

  def lessThan(self, other):
    # return True if the average of self is less than the
    # average of other; else return False

    if self.getAverage() < other.getAverage(): # compare averages
        return True
    else:
        return False

  def compare(self, other):
    # compare the average of self with the average of other
    # return one of:
    # less than
    # equal
    # greater than

    if self.lessThan(other): # less than
        return "less than"
    elif self.equal(other): # equal to
        return "equal to"
    elif self.greaterThan(other): # greater than
        return "greater than"
    else: # something went wrong; could not compare
        return "Error: comparison could not be made"
