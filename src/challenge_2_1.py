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

    # Account name      Account id
    # John              1
    # John              2
    # Mary              3
    # John              4
    # Mary              5
    # Kevin             6
    # Mary              7
    # John              8

    # Account id     Related account
    # 1              2, 8
    # 2              1, 8
    # 3              5, 7
    # 4
    # 5              3, 7
    # 6
    # 7              3, 5
    # 8              1, 2

    accounts_by_id = [{"id": index, "name": a[0], "emails": a[1:]} for index, a in enumerate(array_accounts, start=1)]
    print(accounts_by_id)
    accounts_with_relationship = {}
    for a in accounts_by_id:
        found_relationship = False
        a_index = str(a['id'])
        for b in accounts_by_id:
            b_index = str(b['id'])
            if a_index == b_index:
                # same element > skip analysis
                continue
            else:
                for email in a['emails']:
                    if email in b['emails']:
                        found_relationship = True
                        if accounts_with_relationship.get(a_index) is None:
                            accounts_with_relationship[a_index] = []
                        accounts_with_relationship[a_index].extend(b_index)
        if not found_relationship:
            accounts_with_relationship[a_index] = []

    print(accounts_with_relationship)


    def merge_accounts(accounts, account_id_, related_accounts_):
        current_account = next(filter(lambda x: x['id'] == int(account_id_), accounts), None)
        for i in related_accounts_:
            related_account_ = next(filter(lambda x: x['id'] == int(i), accounts))
            current_account['emails'].extend(related_account_['emails'])
        current_account['emails'] = sorted(set(current_account['emails']))
        return current_account

    for account_id, related_accounts in accounts_with_relationship.items():
        print(account_id, related_accounts)

    analyzed_ids = []
    final_accounts = []
    for account_id, related_accounts in accounts_with_relationship.items():
        if account_id not in analyzed_ids:
            analyzed_ids.append(account_id)
            if related_accounts:
                final_accounts.append(merge_accounts(accounts_by_id, account_id, related_accounts))
                analyzed_ids.extend(related_accounts)
            else:
                final_accounts.append(next(filter(lambda x: x['id'] == int(account_id), accounts_by_id)))

    # print(final_accounts)
    clean_accounts = [[a['name'], *a['emails']] for a in final_accounts]

    print("\nFinal accounts\n****************")
    for a in clean_accounts:
        print(a)




