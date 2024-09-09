
class Solution:
    def sortSocialMediaFeed(self, feed):
        input_feed = [items.split(",") for items in feed]
        print(input_feed)
        input_feed.sort(key=lambda x: (x[1], x[0]))
        print(input_feed)
# Example usage
feed = ["1654162021,user2,Post A", "1654163021,user1,Post B", "1654146021,user1,Post C", "1654165021,user2,Post D"]
s = Solution()
sorted_feed = s.sortSocialMediaFeed(feed)
print(sorted_feed)