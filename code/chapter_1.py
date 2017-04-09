from __future__ import division
from collections import Counter, defaultdict
"""Writing code from scratch without using build-in libraries"""
#dictionary of user ids and names
users = [
    {"id": 0, "name": "Hero" },
    {"id": 1, "name": "Dunn" },
    {"id": 2, "name": "Sue" },
    {"id": 3, "name": "Chi" },
    {"id": 4, "name": "Thor" },
    {"id": 5, "name": "Clive" },
    {"id": 6, "name": "Hicks" },
    {"id": 7, "name": "Devin" },
    {"id": 8, "name": "Kate" },
    {"id": 9, "name": "Klein" }
]
print "****how to index a list of dicts***"
print users[0]["name"]
print "**************************"
#friendships between users by id tuple connection
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                   (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

print "****how to index a list of tuples***"
print friendships[1]
print [ tuplepoint for tuplepoint in friendships]
print "***********************************"

#create list of friends for every user in dict and initialize it to empty
for user in users:
    user["friends"] = []
    print "****how to append empty list of friends***"
    print user
#append list of friends to every entry in the dict
print "user friends list"
for i,j in friendships:
    users[i]["friends"].append(users[j])
    print users[i]
    users[j]["friends"].append(users[i])
    print users[j]
#return number of friends in friends list
def number_of_friends(user):
    """How many friends does _user_ have?"""
    return len(user["friends"])
#total number of frieds for all users
total_connections = sum(number_of_friends(user)
                         for user in users )
print "total_connection"
print total_connections

#number of users in dict
num_users = len(users)
#average friendships connections
avg_connections = total_connections/num_users
#create a list (user_id, number_of_friends)

num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]

print "num_friends_by_id"
print num_friends_by_id

sorted(num_friends_by_id,
       key=lambda (user_id, num_friends): num_friends,
       reverse=True)

print "Sorted num_friends_by_id"
print num_friends_by_id

def friends_of_friends_ids_bad(user):
    #foaf is short for "friend of a friend"
    return [foaf["id"]
            for friend in user["friends"]
            for foaf in friend["friends"]]


print friends_of_friends_ids_bad(users[0]) # [0, 2, 3, 0, 1, 3]
print [friend["id"] for friend in users[0]["friends"]] #[1,2]
print [friend["id"] for friend in users[1]["friends"]] #[0,2,3]
print [friend["id"] for friend in users[2]["friends"]] #[0,1,3]


def not_the_same(user, other_user):
    """two users are not the same if they have different ids"""
    return user["id"] != other_user["id"]
def not_friends(user, other_user):
    """other_user is not a friend if he is not in user["friends"];
    that is, if he is not_the_same as all the people in user["friends"]"""
    return all(not_the_same(friend, other_user ) for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]
                   for foaf in friend["friends"]
                   if not_the_same(user,foaf)
                   and not_friends(user, foaf))
print friends_of_friend_ids(users[3])

interests = [
        (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
        (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
        (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
        (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
        (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
        (3, "statistics"), (3, "regression"), (3, "probability"),
        (4, "machine learning"), (4, "regression"), (4, "decision trees"),
        (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
        (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
        (6, "probability"), (6, "mathematics"), (6, "theory"),
        (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
        (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
        (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
        (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

#This is exhustive because it goes through all interests list for every search
def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]
#if we want to be fast we should index interests list to  with user ids

user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# keys are user_ids, values are lists of interests for that user_id

interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(interested_user_id
                   for interest in interests_by_user_id[user["id"]]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user["id"])

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                            (48000, 0.7), (76000, 6),
                            (69000, 6.5), (76000, 7.5),
                            (60000, 2.5), (83000, 10),
                            (48000, 1.9), (63000, 4.2)]
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
    tenure :  sum(salaries)/len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}
# it might be helpful to bucket the tenures:

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

average_salary_by_bucket = {
    tenure_bucket :  sum(salaries)/len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.iteritems()
}

def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"

words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split())
for word, count in words_and_counts.most_common():
    if count > 1:
        print word, count
