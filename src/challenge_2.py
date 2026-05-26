# Problem:  Account Email Merging Algorithm
# We need to implement a Node.js (or whatever language)  function that merges user accounts based on
# shared email addresses within the same name group.
#
# Requirements:
# Group accounts by person name (first element in each array)
# Within each name group, merge accounts that share any email addresses
# Return merged accounts with all unique emails sorted alphabetically
# Keep accounts with no shared emails as separate entries
# Input Format:
# [["Name", "email1", "email2", ...], ["Name", "email1", "email3", ...], ...]
#
# Input: [
#   ["John","johnsmith@mail.com","john_newyork@mail.com"],
#   ["John","johnsmith@mail.com","john00@mail.com"],
#   ["Mary","mary@mail.com"],
#   ["John","johnnybravo@mail.com"]
# ]
# Expected Output: [
#   ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
#   ["Mary","mary@mail.com"],
#   ["John","johnnybravo@mail.com"]
# ]
#
# Logic:
# First two John accounts share "johnsmith@mail.com" → merge into one account
# Third John account has no shared emails → remains separate
# Mary account has no duplicates → remains unchanged
from typing import List, Dict, Optional


class Account:
    def __init__(self, id_, array):
        self._id = id_
        self._name = array[0]
        self._emails: List[str] = array[1:]
        self._related_accounts: List[Account] = []
        self._status: Optional[str] = None

    def id(self):
        return self._id

    def name(self):
        return self._name

    def emails(self):
        return sorted(set(self._emails))

    def related_accounts(self):
        return self._related_accounts

    def status(self):
        return self._status

    def has_related_accounts(self):
        return len(self._related_accounts) > 0

    def set_as_original(self):
        self._status = "original"
        for related_account in self.related_accounts():
            self._emails.extend(related_account.emails())
            related_account.set_as_merged()

    def set_as_merged(self):
        self._status = "merged"

    def is_merged(self):
        return self._status == "merged"

    def is_original(self):
        return self._status == "original"

    def analyse_related_accounts(self, accounts: List["Account"]):
        for account in accounts:
            print(f"To analyse if {account.name()}({account.id()}) is related to {self.name()}({self.id()})")
            for email in self.emails():
                if email in account.emails():
                    print(f"{account.name()}({account.id()}) is related to {self.name()}({self.id()})")
                    self._related_accounts.append(account)

    def __repr__(self):
        return f"{self.name()}(id:{self._id}, emails:{str(self.emails())})"

if __name__ == '__main__':
    array_accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John","john00@mail.com","johnsmith@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"],
        ["Mary", "mary1@mail.com", "mary2@mail.com", "mary@mail.com", "mary3@mail.com"],
        ["Kevin", "kevin@test.com", "kevin@foo.io"],
        ["Mary", "mary4@mail.com", "mary5@mail.com", "mary@mail.com", "mary6@mail.com"],
        ["John", "johnsmith@mail.com"],
    ]
    array_obj_accounts: List[Account] = [Account(index, o) for index, o in enumerate(array_accounts)]
    for account_obj in array_obj_accounts:
        print(account_obj)
    print("*" * 200 + "\n")

    for account_obj in array_obj_accounts:
        print(f"To analyse {account_obj.name()}")
        account_obj.analyse_related_accounts([a for a in array_obj_accounts if a.id() != account_obj.id()])

    print("\nRelated accounts\n****************")
    for account_obj in array_obj_accounts:
        print(f"{account_obj.name()}(id:{account_obj.id()}) -> related accounts: {account_obj.related_accounts()}")

    for account_obj in array_obj_accounts:
        if not account_obj.is_merged():
            account_obj.set_as_original()

    final_accounts = [[a.name(), *a.emails()] for a in array_obj_accounts if a.is_original()]

    print("\nFinal accounts\n****************")
    for a in final_accounts:
        print(a)

    # dict_accounts_by_name: Dict[str, List[Account]]= {}
    # for account in array_obj_accounts:
    #     if account.name() not in dict_accounts_by_name.keys():
    #         dict_accounts_by_name[account.name()] = []
    #     dict_accounts_by_name[account.name()].append(account)
    #
    # for k,v in dict_accounts_by_name.items():
    #     print(f"{k} -> {v}")
    # print()
    # print(dict_accounts_by_name)
    #
    # merged_accounts: Dict[str, List[str]]= {}
    # for k, v in dict_accounts_by_name.items():
    #     print(f"To analyse accounts for {k}")
    #     for account in v:
    #         print(account)




    # results = [array_obj_accounts[0]]
    # result_index = 0
    # for account in array_obj_accounts[1:]:
    #     current_result_account = results[result_index]
    #     current_result_account.try_merge(account)

    # Account id
    # Account name
    # John              1
    # John              2
    # John              3
    # Mary              4

    # Related account
    # Email
    # johnsmith@mail.com        1, 2
    # john_newyork@mail.com     1
    # johnsmith@mail.com.       2
    # john00@mail.com           2
    # johnnybravo@mail.com      3
    # mary@mail.com             4
