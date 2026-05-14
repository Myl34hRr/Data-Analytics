{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bca6a496-81eb-4c2f-9db9-faddfffee54d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0a258e01-5ea5-4a41-8c78-a10acd64ab04",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "randint(1, 10): 3\n"
     ]
    }
   ],
   "source": [
    "# 1. random.randint(a, b) Random integer between a and b (inclusive)\n",
    "print(\"randint(1, 10):\", random.randint(1, 10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "aa6e46c7-124e-4659-b592-1bdd14a32223",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "random(): 0.2985807983170038\n"
     ]
    }
   ],
   "source": [
    "# 2. randon.random() random float between 0.0 and 1.0\n",
    "print(\"random():\", random.random())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2bb423e3-7015-4436-8af7-865d82781490",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "choice(fruits): apple\n"
     ]
    }
   ],
   "source": [
    "# 3. random.choice(seq) random single element from a sequence\n",
    "fruits =[\"apple\", \"banana\", \"cherry\"]\n",
    "print(\"choice(fruits):\", random.choice(fruits))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b0202dfb-9641-4f5a-880a-4bd6ee6a8eaa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "choices(fruits, K=2): ['cherry', 'apple', 'banana']\n"
     ]
    }
   ],
   "source": [
    "# 4. random.choices(seq, K=n) list of K random elements(with replacement)\n",
    "print (\"choices(fruits, K=2):\", random.sample(fruits, k=3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d27194df-47c6-486f-80f3-36024617ae27",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sample(fruits, K=2): ['cherry', 'banana']\n"
     ]
    }
   ],
   "source": [
    "# 5. random.sample(seq, K=n) list of K unique random elements(whitout replacement)\n",
    "print(\"sample(fruits, K=2):\", random.sample(fruits, k=2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a9ad0362-4ce7-4f93-ae71-c6ce67664615",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "shuffled numbers: [1, 4, 5, 3, 2]\n"
     ]
    }
   ],
   "source": [
    "# 6. random.shuffle(seq) shuffles a list in place\n",
    "numbers=[1, 2, 3, 4, 5]\n",
    "random.shuffle(numbers)\n",
    "print(\"shuffled numbers:\", numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96b8f4d6-6b4e-427d-b425-0b72f3c936a9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
