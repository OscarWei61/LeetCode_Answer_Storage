
class Solution:
    def sortSocialMediaFeed(self, feed):
        # Split the input feed into individual components: timestamp, userId, and post
        input_feed = [items.split(",") for items in feed]
        
        # Sort the feed first by userId, and then by timeStamp (both in ascending order)
        input_feed.sort(key=lambda x: (x[1], x[0]))
        
        # Join the sorted components back into strings
        sorted_feed = [",".join(item) for item in input_feed]
        
        return sorted_feed
# Example usage
feed = ["1654162021,user2,Post A", "1654163021,user1,Post B", "1654146021,user1,Post C", "1654165021,user2,Post D"]
s = Solution()
sorted_feed = s.sortSocialMediaFeed(feed)
print(sorted_feed)