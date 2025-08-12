#!/bin/bash
# This script was generated to transcribe all sermon audio files.
# It will download audio files and transcribe them using Whisper.

mkdir -p transcripts

echo "Transcribing: No Turning Back"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100530-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: A Better Sanctuary"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100620-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Humility Rewarded"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100321-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Healing Prayer Seminar: Session 5"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/HPS10-5-low.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: A Better Covenant"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100613-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: An Eternal High Priest"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100606-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: The True Priest"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100523-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: The True Rest"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100516-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: Greater than Moses"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100509-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Truly Human"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100502-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Greater than Angels"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100425-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: Son of God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100418-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Resurrection & Ascension"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100411-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good Friday"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100402-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Power to Save and to Heal"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100328-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Healing Prayer Seminar: Session 4"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/HPS10-4-low.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Healing Prayer Seminar: Session 3"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/HPS10-3-low.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Healing Prayer Seminar: Session 2"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/HPS10-2-low.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Healing Prayer Seminar: Session 1"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/HPS10-1-low.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Humble before God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100314-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Persistent Widow"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100307-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Ready for Christ’s Return"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100228-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Real Converts"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100221-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Responsible Servants"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100214-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Lazarus and the Rich Man"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100207-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Divided Loyalties"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100131-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Serve One Master"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100124-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Lost Son"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100117-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Lost Sheep"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100110-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Epiphany: Christ Revealed"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100103-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus Grows in Wisdom and Stature"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon091227-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: What’s so special about Jesus?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon091225-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Press On In Christ"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon091220-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Contentment & Generosity"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon091213-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Don’t Shrink Back"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100704-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: A Better Sacrifice"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100627-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Keep Believing"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100718-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Keep Running The Race"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100725-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How can we be sure faith is not a delusion?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100801-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: What does God think of the environment?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon100808-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Trust Christ"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon091206-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Faith in Christ"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon091122-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Model Christ"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon091115-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Shine Like the Stars"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon091108-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Shine Like Stars (Story)"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon091101-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Be Worthy of Christ"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon091025-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Live for Christ"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon091018-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Speak About Christ"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon091011-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Grace In Christ"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon091004-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Blind Man Healed"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090927-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Serving God in Tanzania"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090920-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Why suffering: A Theological Response?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-08-15-WhySufferingATheologicalResponse.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Why does Jesus tell stories?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-08-15-WhyDoesJesusTellsStories.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Will we meet our loved ones in heaven (assuming we've all made it)?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-08-22-WillWeMeetOurLovedOnesInHeaven.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Keep on Going"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-08-29-KeepOnGoing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Keep On Loving"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-09-05-KeepOnLoving.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Women's Weekend - Eternity 1"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-WomensWeekend-Eternity-Session1.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Women's Weekend - Eternity 2"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-WomensWeekend-Eternity-Session2.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Women's Weekend - Eternity 3"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-WomensWeekend-Eternity-Session3.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Women's Weekend - Eternity 4"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-WomensWeekend-Eternity-Session4.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Women's Weekend - Eternity 5"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-WomensWeekend-Eternity-Session5.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Really, how near is the kingdom?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-09-12-ReallyHowNearIsTheKingdom.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Prayer For Healing"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-09-19-PrayerForHealing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to Sustain Spiritual Momentum"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090913-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Motivations for Mission"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-09-26-MotivationsForMission.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Grief and Loss Seminar"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/GriefAndLoss100601-low.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: What Have We Learned?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090906-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Made for Mission"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090830-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Shaped for Serving God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090823-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Created to Become Like Christ"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090816-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Formed for God's Family"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090809-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Worship is Knowing God and Loving Him Back"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090802-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Breakfast with Tim Costello"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Breaky090801l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: What On Earth Am I Here For?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090726-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Don't Waste Your Life."
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090719-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Trust God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090705-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Develop Discipline"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090426-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Marry Well"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090628-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Build Strong Families"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090621-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Manage Anger"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090614-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Prophecy"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090531-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Be Generous"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090524-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Speak Truth"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090517-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Work Honestly"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090510-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Take Initiative"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090503-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Pursue Wisdom"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090419-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Feast Of Trumpets"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-10-03-TheFeastOfTrumpets.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Resurrection of Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090412-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Cross of Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090410-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Divisiveness of Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090405-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Compassion of Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090322-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Faith in Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090315-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Challenge of Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090308-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Blasphemy of Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090301-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Power of Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090222-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Disciples of Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090215-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Prayers - Response to bushfires"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Prayers-ResponseToBushfires0902-l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Dedication Sunday"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090201-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Great is the Lord"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090125-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hope for a Broken World"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090118-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: You Know Me"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon090104-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Daniel: Surviving the Education System"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-10-10-DanielSurvivingTheEducationSystem.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Daniel: Consulting To A Powerbroker"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-10-17-Daniel-ConsultingToAPowerbroker.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Women's Brunch"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-10-16-WomensBrunch.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Daniel: Passive Resistance When Your Life is at Risk"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-10-24-Daniel-PassiveResistanceWhenYourLifeIsAtRisk.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Gift of a New Start"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon081228-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Gift of Joy"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon081214-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christmas Day"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon081225-0930l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christmas Eve"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon081224-23l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Gift of Strength"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon081221-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Gift of Purpose"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon081207-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Gift of Hope"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon081130-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Celebrate Together"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon081109-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Every Day"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon081102-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Disability-Friendly Church"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-10-31-ADisabilityFriendlyChurch.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Prodigal God: The Heart of the Christian Faith"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-10-31-TheProdigalGod-TheHeartOfTheChristianFaith.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Daniel: Madness at the Top of the Government"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-11-07-Daniel-MadnessAtTheTopOfTheGovernment.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Daniel: When the Writing’s On the Wall"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-11-14-Daniel-WhenTheWritingsOnTheWall.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Daniel: Politics and the Lion's Den"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-11-21-Daniel-PoliticsAndTheLionsDen.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to choose? How to decide?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-11-20-MensBreakfast-HowToChooseHowToDecide.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Be a Servant"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon081026-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Don't Forget"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon081019-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Join In"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon081012-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Be a Blessing"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon081005-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Living Stones"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080928-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's People Must Persevere"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080921-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Daniel: God’s Government"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-11-28-Daniel-GodsGovernment.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Birth of Moses"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-12-12-TheBirthOfMoses.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Birth of John the Baptist"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-12-19-TheBirthOfJohnTheBaptist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Birth Of Jesus (Christmas Eve)"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-12-24-ChristmasEve-TheBirthOfJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Future of S@6"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-12-05-TheFutureOfSat6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Birth Of Jesus (Christmas Day)"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-12-25-ChristmasDay-TheBirthOfJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Simeon “Sees” Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2010-12-26-SimeonSeesJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Daniel: Evil Government and God's Response"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-01-02-Daniel-EvilGovernmentAndGodsResponse.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Daniel: A Vision of the End"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-01-09-Daniel-AVisionOfTheEnd.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's People Celebrate a New Beginning"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080914-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's People, One God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080907-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's People Confess"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080831-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's People Celebrate God's Word"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080824-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Place Rebuilt"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080817-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's People Challenged"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080810-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God Directs and Protects"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080803-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God Gives Success"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080727-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God Begins the Project"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080720-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Invitation"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080706-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Who will Jesus Save?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080629-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Delighted to Heal"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080622-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Get Right with God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080615-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Judge What is Right"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080608-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: the Great Divider"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080601-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Get Ready"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080525-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Don't Worry"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080518-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Eat, Drink and Be Merry"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080504-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Safe Forever"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080427-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to Pray about Your Problems"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080420-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Daniel: Praying For A Better Future"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-01-16-Daniel-PrayingForABetterFuture.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Daniel: The God of the Nations"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-01-23-Daniel-TheGodOfTheNations.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Daniel: Future Conflict & Future Hope"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-01-30-Daniel-FutureConflictAndFutureHope.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Daniel, the New Testament & Us"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-02-06-Daniel-TheNewTestamentAndUs.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Equipping God’s People for Ministry"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-02-13-EquippingGodsPeopleForMinistry.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Homosexuality #1: What does the Bible say?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-02-20-Homosexuality1-WhatDoesTheBibleSay.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Climate Change"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Breaky0804l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to Develop Patience"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080413-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How To Face Your Future"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080330-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How To Be Wise With Your Wealth"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080406-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Resurrection"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080323-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good Friday"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080321-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How To Quit Playing God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080316-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How To Avoid Arguments"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080309-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How To Manage Your Mouth"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080224-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How To Have Real Faith"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080217-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How To Treat People"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/AA_sermon080210.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How To Be Blessed By The Bible"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080203-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How To Win Over Temptation"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080127-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How To Make Up Your Mind"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080120-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How To Profit From Your Problems"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080113-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Marks Of a Mature Person"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon080106-10l.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News For Ever"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon071230-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christmas Reflections"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon071224-23.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News For Smart People"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon071223-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News For Simple People"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon071216-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Our Weakness, God’s Power"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-02-27-OurWeaknessGodsPower.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Why Promote The Gospel?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-03-06-WhyPromoteTheGospel.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Our Hidden Mission: Promoting The Gospel Through Our Prayer"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-03-13-OurHiddenMissionPromotingTheGospel.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Being the Light of the World"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-03-21-BeingTheLightOfTheWorld.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Sex and the Internet"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon071209-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Celebrate Together"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon071209-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: When Can I Have Sex In Church"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon071202-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News for Mary"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon071202-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Who Gets Good Sex?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon071125-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Whom Have I in Heaven But You?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon071118-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Protection"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon071111-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's King"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon071104-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Character"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon071028-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Place"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon071028-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Work and Our Work"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon071021-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Mercy"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon071014-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Being Beautiful People: Promoting the Gospel through Christian Behaviour"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-03-27-BeingBeautifulPeoplePromotingTheGospelThroughChristianBehaviour.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Homosexuality #2: Theological and Pastoral Issues"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-03-01-Homosexuality2-TheologicalAndPastoralIssues.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Partners for Life: Promoting the Gospel with our Money"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-04-03-PartnersForLife-PromotingTheGospelWithOurMoney.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Conversation Ready: Promoting the Gospel in Daily Conversation"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-04-10-ConversationReady.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Heralds Together: Promoting The Gospel through our Public Worship"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-04-17-HeraldsTogether.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: What Must I Do To Be Loved"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-04-17-WhatMustIDoToBeLoved.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Cross of Christ"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-04-22-TheCrossOfChrist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Reflection on the Resurrection"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-04-24-ReflectionOnTheResurrection.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hearing God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Hearing_God_20110404.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Question of Glory"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-05-01-AQuestionOfGlory.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Question of Power"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-05-08-AQuestionOfPower.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Where is God in Fukushima?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-05-07-WhereIsGodInFukushima.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Question of Greatness"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-05-15-AQuestionOfGreatness.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Question of Greatness"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-05-15-AQuestionOfGreatness-6PM.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Confirmation & Reception"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-05-29-ConfirmationAndReception.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Question Of Divorce"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-06-05-AQuestionOfDivorce.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Worship and the Arts (Part 1 of 2)"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-06-12-WorshipAndTheArts-Part1of2.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Worship and the Arts (Part 2 of 2)"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-06-12-WorshipAndTheArts-Part2of2.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Question of the Heart"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-06-09-10-AQuestionOfTheHeart.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Question of Life and Death"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-06-26-10-AQuestionOfLifeAndDeath.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Question of Sight"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-07-03-10-AQuestionOfSight.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Commissioning The Littles"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-06-26-CommissioningOfTheLittles.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Moving Sunday"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon071007-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hope"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070923-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Genesis and Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070916-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hope for the Future"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070909-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Joseph and Jacob"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070902-09.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Joseph and Brothers in Egypt"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070826-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Power and Success"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070819-09.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Sex and Power"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070812-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Judah and Tamar"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070805-09.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Spotlight On Mission"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-07-10-SpotlightOnMission.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Joseph's Coat of Many Troubles"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070729-09.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Community"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070722-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Hope"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070715-11.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Behaviour"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070708-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Ministry"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070701-09.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Evangelism"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070624-09.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Friendships"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-07-17-RedeemingRelationshipsChristianFriendships.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jacob's God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070617-09.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Rape and Revenge"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070610-09.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jacob's Struggle"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070603-09.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Family Pentecost Service"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070527-11.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jacob's Family"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070520-09.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jacob's Dream"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070513-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jacob's Deception"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070506-11.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jacob's Election"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070429-11.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to Discover My Ministry"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070422-09.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Made to Minister"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070415-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Celebration of the Resurrection"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070408-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good Friday"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070406-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus Came to Die"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070401-09.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Sight and Insight"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070325-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus Feeds 4000"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070318-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus Does Everything Well"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070311-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Love God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070304-11.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Spread the Love Around"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070225-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Spread the Love Around"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070225-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Take Courage"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070128-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Invest Yourself"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070218-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Deepen the Foundations"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070211-09.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Get Connected"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070204-09.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Feasting with King Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070121-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Feasting with the Wrong King"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070114-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Representing the King"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon070107-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Workplace Relationships"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-07-24-18-RedeemingRelationshipsChristianWorkplaceRelationships.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christians Falling In Love"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-07-31-10-RedeemingRuthChristiansFallingInLove.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Power and Promise of Redeeming Relationships"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-08-07-10-RedeemingRuthThePowerAndPromiseOfRedeemingRelationships.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Redeeming Marriages"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-08-14-10-RedeemingMarriages.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Redeeming Singlehood"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-08-21-18-RedeemingSinglehood.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: All Age Service"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-08-21-10-AllAgeService.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Redeeming Marriages (6PM)"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-08-14-18-RedeemingMarriages.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Holy Spirit Gives Life"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-08-28-TheHolySpiritGivesLife.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Looking Back, Looking Forward"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon061231-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A King? You Must Be Joking!"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon061231-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Son is Born"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon061225-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Simeon"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon061224-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Quiet Christmas"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon061217-2.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: 'Tis the Season to be Jolly"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon061217-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Gift of a Cosmic Plan"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon061210-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: 'Tis the Season to be Looking Good"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon061203-09.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Who is my Neighbour in a Global Village"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon061119.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Dinner: Men Under Pressure"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/MensDinner061111.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Getting Godly Government"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon061112-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Holy Spirit Helps us in our Weakness"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-09-04-10-TheHolySpirirtHelpsUsInOurWeakness.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God’s eternal commitment to His People"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-09-11-18-GodsEternalCommitmentToHisPeople.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Fishing at Dawn"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-09-18-10-FishingAtDawn.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Finding Renewal in the Midst of Wreckage!"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-09-19-20-FindingRenewal.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The compassion of God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-09-18-18-TheCompassionOfGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Psalm 103"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-10-02-10-Psalm103.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Maddening Mercy of God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon061105-09.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God Loves Godless Cities!"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon061029-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Out of the Blue - Depression"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Depression%20061101.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: What Every Man Needs to Know."
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/mensbreaky061028.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Trust God for the Future of St Alfred's"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon061022-11.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Only God Can Save You!"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon061015-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Worship in Spirit and Truth"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon061008-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God Will Find You!"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon061008-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Mission in Action"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060924-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News Locally and Globally"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060917-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News for the AFL"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060910-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Features of a Cult"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060910-11.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hold on to Hope"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060903-09.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hope for the Future"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060827-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hope for the Future"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060827-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Freed by the Spirit"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060820-11.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Released from the Law"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060813-11.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Freed from Sin"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060806-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Peace with God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060730-11.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Key of Faith"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060723-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Faith in the Firing Line"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/mensbreaky060722.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Solution"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060716-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Psalm 51"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-10-09-10-Psalm51.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Psalm 84"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-10-09-18-Psalm84.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Emperor's New Clothes"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060709-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Where to Keep Your Treasure"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060702-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Where to Keep Your Treasure"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060702-11.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Sowing the Word, Harvesting the Nations"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060625-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Words of Blessing"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060625-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: What it means to be a Jew"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060618-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God is a Fair Judge"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060611-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Judgement on Sin"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060604-11.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Introduction to Romans"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060528-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Precious Words"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060521-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to Deal with Disappointment"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060521-11.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to Pass Life's Greatest Tests"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060514-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Powerful Words"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060507-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: What To Do When You Feel Like Giving Up"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060507-11.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Features of a Cult"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060430-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: It's Never Too Late to Start Again"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060430-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Proverbs - Words of Blessing"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060423-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Don't Let Your Doubts Defeat You"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060423-11.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Resurrection"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060416-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Death of Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060414-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus Prays for All Believers"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060409-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Psalm 139"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-10-16-10-Psalm139.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Psalm 19"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-10-16-18-Psalm19.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus Prays for His Friends"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060402-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus Prays for His Friends"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060402-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: What's your Game?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060326-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Sorting Out the Medals"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060326-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Run to Win"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060319-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Joy and Peace of Seeing Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060312-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Work of the Holy Spirit"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060305-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to Overcome Opposition"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060226-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How To Bear Fruit That Will Last"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060226-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Father Son and Spirit"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060219-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Game Plan for Your Life"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/mensbreaky060218.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: The Way To The Father"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060212-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Amazing Love"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060205-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Continue to the End"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060205-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: What God Expects of Church Leaders"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060129-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How You Can Be Fit For God's Work"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060122-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Be Strong in Christ Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060115-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Do Not Be Ashamed of the Gospel"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060108-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Keep Going!"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon060101-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Royal Presence"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon051218-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Psalm 73"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-10-02-18-Psalm73.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God’s Merciful Choice"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-10-23-10-GodsMercifulChoice.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Who Do You Say Jesus Is?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon051225-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Royal Visit"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon051211-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Royal Visit"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon051211-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Of Royal Descent"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon051204-6.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Of Royal Descent"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/Sermon051204-9.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Everyone Who Calls on the Name of the Lord will be Saved"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-10-30-10-EveryOneThatCallsOnTheNameOfTheLordWillBeSaved.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Thorny Question of Predestination"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-11-06-10-TheThornyQuestionOfPredestination.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Faith Comes from Hearing the Message"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-11-13-10-FaithComesFromHearingTheMessage.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Mercy Triumphant"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-11-20-10-MercyTriumphant.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Advent - All Age Service"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-11-27-10-AdventAllAgeService.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Glory of the Lord Shall be Revealed"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-12-04-10-TheGloryOfTheLordShallBeRevealed.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God is the Potter, We Are the Clay"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-11-27-18-GodIsThePotterWeAreTheClay.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Lord Has Done Great Things"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-12-11-10-TheLordHasDoneGreatThings.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Your Saviour Comes"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-12-18-10-YourSaviourComes.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christmas Day Reflection - Peace"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-12-25-10-ChristmasReflection-Peace.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christmas Eve Reflection - Hope"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-12-24-23-ChristmasEveReflection-1of4-Hope.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christmas Eve Reflection - Joy"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-12-24-23-ChristmasEveReflection-2of4-Joy.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christmas Eve Reflection - Peace"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-12-24-23-ChristmasEveReflection-3of4-Peace.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christmas Eve Reflection - Love"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2011-12-24-23-ChristmasEveReflection-4of4-Love.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Introducing John and 2012"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-01-01-10-IntroducingJohnAnd2012.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: What We Have Learnt in Tanzania"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-01-22-10-NevilleAndElspethCarrWhatWeHaveLearntInTanzania.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Humility and Prayer"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-01-29-10-Luke18-9-14.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Connect 50"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-02-05-10-Connect50.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God With Us"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-02-12-10-GodWithUs.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus is the Son of God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-02-19-10-JesusIsTheSonOfGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Importance of Men"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-02-18-08-MensBreakfastDougPeteringTheImportanceOfMen.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Following Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-02-26-10-FollowingJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Water Into Wine"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-03-04-WaterIntoWine.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus Clears the Temple"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-03-11-10-JesusClearsTheTemple.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus Offers New Life"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-03-18-18-JesusOffersNewLife.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Life and Light"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-03-25-10-LifeAndLight.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Life or Death"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-04-01-10-LifeOrDeath.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Death of Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-04-06-10-TheDeathOfJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Saviour of the World"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-04-15-10-TheSaviourOfTheWorld.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus Heals a Boy"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-04-22-10-JesusHealsABoy.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Meaning of Easter"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-04-08-18-TheMeaningOfEaster.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus Heals a Man"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-04-29-10-JesusHealsAMan.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus The Life Giver"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-05-06-10-JesusTheLifeGiver.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: You Can Believe Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-05-13-10-YouCanBelieveJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Breakfast with Dale Sheppard"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-05-12-08-MensBreakfastDaleSheppard.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: You Can Believe Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-05-13-18-YouCanBelieveJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Anointing of Jesus Feet"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-05-20-18-TheAnointingOfJesusFeet.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Wonder-Worker, Prophet or King?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-05-27-10-WonderWorkerProphetOrKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Bread of Life"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-06-03-10-TheBreadOfLife.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to Grow the Kingdom of God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-05-27-18-HowToGrowTheKingdomOfGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: To Follow or Give Up?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-06-10-10-ToFollowOrGiveUp.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: On Earth As in Heaven?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-06-17-10-OnEarthAsInHeaven.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Religion Poisons"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-06-24-10-ReligionPoisons.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Love in the World?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-07-01-10-GodsLoveInTheWorld.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: What Can We Do?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-07-08-10-WhatCanWeDo.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: So What Next?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-07-15-10-SoWhatNext.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Turning to a Different Gospel"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-07-22-10-TurningToADifferentGospel.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Gospel-Changed Life"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-07-29-10-AGospelChangedLife.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Gospel to the Nations"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-08-05-10-AGospelToTheNations.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Living The Gospel"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-08-12-10-LivingTheGospel.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: All-Age Service"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-08-19-10-All-Age-Service.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Farewell to Wei-Han (10am)"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-08-19-10-Wei-Han-Farewell.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Farewell to Wei-Han (6pm)"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-08-19-18-Wei-Han-Farewell.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Global perspective of the church's mission in the 21st Century"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/EFAC-2012-07-16-AbpKwashi.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Gospel and Faith"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-08-26-10-TheGospelAndFaith.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Connect50 Update"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-09-02-10-Connect50Update.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Gospel and the Law"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-09-09-10-TheGospelAndTheLaw.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Farewell to Kieran"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-09-02-18-Kieran-Farewell.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Children of God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-09-17-10-ChildrenOfGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Elephant in the Room, Part 1: The issues, a story and changing the culture"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-09-15-Part1-ElephantInTheRoom.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Elephant in the Room, Part 2: Dealing with porn"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-09-15-Part2-ElephantInTheRoom.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Elephant in the Room, Part 3: Q & A"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-09-15-Part3-ElephantInTheRoom.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Never Go Back"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-09-25-10-NeverGoBack.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Psalm 67: The God of the Nations"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-09-30-10-TheGodOfTheNations.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Psalm 33: The God of Creation"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-10-07-10-TheGodOfCreation.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Baptism Service"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-10-14-10-BaptismService.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Prayer for Healing"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-10-21-10-PrayerForHealing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Children of Promise"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-10-21-18-ChildrenOfPromise.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel Freedom"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-10-28-10-GospelFreedom.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel Character"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-11-04-10-GospelCharacter.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel Relationships"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-11-11-10-GospelRelationships.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Journeys in Regreening"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-11-17-JourneysInRegreening.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Sowing and Reaping"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-11-18-10-SowingAndReaping.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Steadfast Love of God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-11-25-18-TheSteadfastLoveOfGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: 1 John 1"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-12-02-18-1John1.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Keep Watch Because Jesus Will Return"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-12-09-10-KeepWatchBecauseJesusWillReturn.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Local Churches On Mission Together 2012"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-12-16-10-LocalChurchesOnMissionTogether.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Keep the Faith and Win the Prize"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-12-23-10-KeepTheFaithAndWinThePrize.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christmas Eve 2012"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-12-24-23-ChristmasEve.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christmas Day 2012"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2012-12-25-10-ChristmasDay.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Heaven’s Song"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-01-06-10-HeavensSong.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Zechariah's Song"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-01-13-10-ZechariahsSong.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Simeon's Song"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-01-20-18-SimeonsSong.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hallelujah!"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-01-27-10-Hallelujah.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How the Mighty have Fallen"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-02-03-10-HowTheMightyHaveFallen.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: David: Shepherd & King"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-02-10-18-DavidShepherdAndKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: David and the Ark"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-02-17-18-DavidAndTheArk.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: An Eternal Kingdom"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-02-24-10-AnEternalKingdom.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Turning Points"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-02-23-MensBreaky-TurningPoints.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: David and Bathsheba"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-03-03-David_n_Bathsheba.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Rape and Revenge"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-03-10-RapeAndRevenge.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Kingdom Lost and Regained"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-03-17-10-KingdomLostAndRegained.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God is My Rock"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-03-24-10-GodIsMyRock.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Cross of Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-03-29-10-TheCrossOfJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Resurrection of Jesus"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-03-31-10-TheResurectionofJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jo's story"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-03-02-WomensMinistry-JoMcNamara.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Power of the Cross"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-04-07-10-ThePowerOfTheCross.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Sin, Sacrifice & the Mercy of God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-04-14-10-SinSacrificeAndTheMercyOfGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Dealing with Doubt"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-03-31-18-DealingWithDoubt.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: Friend"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-04-21-10-JesusFriend.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: Judge"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-04-28-10-JesusJudge.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Prayer for Healing"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-05-05-Prayer_for_Healing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: Rest"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-05-12-10-JesusRest.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: Lord"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-05-19-18-JesusLord.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: Servant"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-05-26-10-JesusServant.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: Good or Evil"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2013-06-02-18-JesusGoodOrEvil.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: Raised"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-06-09-10-JesusRaised.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: True Generosity"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-02-16-10-TrueGenerosity.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's House or Yours?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-06-23-10-GodsHouseOrYours.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: New Family"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-06-16-10-JesusNewFamily.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: Raised"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-06-09-18-JesusRaised.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's House or Yours?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-06-23-18-GodsHouseOrYours.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Be Strong"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-06-30-10-BeStrong.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Be Strong"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-06-30-18-BeStrong.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: An Unshakeable Kingdom"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-07-07-10-AnUnshakeableKingdom.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: An Unshakeable Kingdom"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-07-07-18-AnUnshakeableKingdom.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God is Great"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-07-21-10-GodIsGreat.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Light"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-07-21-18-Light.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: No Divisions!"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-07-28-10-NoDivisions.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: No Divisions!"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-07-28-18-NoDivisions.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Power of God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-08-04-18-ThePowerOfGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Spirit of God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-08-11-10-TheSpiritOfGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: All About Seeds"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-08-19-10-AllAboutSeeds.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Serving Together"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-08-19-18-ServingTogether.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Apostles and Fools"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-08-25-10-ApostlesAndFools.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Sexual Sin in the Church"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-09-01-10-SexualSinInTheChurch.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Sexual Sin in the Church"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-09-01-18-SexualSinInTheChurch.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Disputes Among Christians"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-09-08-10-DisputesAmongChristians.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Disputes Among Christians"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-09-08-18-DisputesAmongChristians.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Sexual Immorality"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-09-15-10-SexualImmorality.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Marriage is Good"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-09-22-10-MarriageIsGood.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Psalm 30"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-09-29-10-Psalm30.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: 1 Peter 5"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-09-29-18-1Peter5.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Thomas Cranmer: Hero of Faith"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-10-06-10-HeroOfFaith.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Singleness is Good"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-10-13-10-SinglenessIsGood.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Remain as you Are"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-10-13-18-RemainAsYouAre.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Voice to the Voiceless"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-10-13-VoiceToTheVoiceless.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Marriage or Singleness: You Decide"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-10-20-10-MarriageOrSingleness.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Singleness is Good"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-10-20-18-SinglenessIsGood.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A New Way of Living"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-10-27-10-ANewWayOfLivingWhereJusticeEvangelismCreationCareHolinessIntersect.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Shadow of the Cross"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-11-03-18-TheShadowOfTheCross.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Worship Fully"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-11-10-10-WorshipFully.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Prayer For Healing"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-11-17-10-PrayerForHealing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God Wants You to Be Rich"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-11-17-18-GodWantsYouToBeRich.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Let no one lose Heart"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-12-01-10-LetNoOneLoseHeart.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Life Lived in Christ"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-12-01-18-LifeLivedInChrist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Spend Less"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-12-08-10-SpendLess.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Give More"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-12-15-10-GiveMore.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Love All"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-12-22-10-LoveAll.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christmas Eve 2013"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-12-24-ChristmasEve.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christmas Day 2013"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-12-25-ChristmasDay.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Seek and Save the Lost"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2013-12-29-10-SeekAndSaveTheLost.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Use What God Gives You"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-01-05-10-UseWhatGodGivesYou.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: The Conquering Hero?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-01-12-10-JesusTheConqueringHero.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Who’s the Boss?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-01-19-10-WhosTheBoss.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Murderous People"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-01-26-10-AMurderousPeople.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Pay Your Taxes"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-02-02-10-PayYourTaxes.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Marriage and the Resurrection"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-02-09-10-MarriageAndTheResurrection.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Freedom And Conscience 1"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-02-23-10-FreedomAndConscience1.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Forfeiting Our Rights"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-03-02-10-ForfeitingOurRights.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Forfeiting Our Rights"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-03-02-18-ForfeitingOurRights.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Training for the Race"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-03-09-10-TrainingForTheRace.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: All for the Gospel"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-03-16-10-AllForTheGospel.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Flee from Idolatry"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-03-23-10-FleeFromIdolatry.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Nepal Mission Trip"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-03-09-18-NepalMissionTrip.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Freedom and Conscience 2"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-03-30-10-FreedomAndConscience.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men and Women in the Church"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-04-06-10-MenAndWomenInTheChurch.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Prayer for Healing"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-04-13-10-PrayerForHealing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good Friday 2014"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-04-18-10-GoodFriday.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Easter Sunday 2014"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-04-20-10-Easter.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Easter Sunday 2014"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-04-20-18-Easter.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Spiritual Gifts"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2014-05-04-10-SpiritualGifts.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Lord's Supper"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-04-27-10-TheLordsSupper.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Spiritual Gifts"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-05-04-18-SpiritualGifts.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Prophecy and Tongues"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-05-18-10-ProphecyAndTongues.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gifts Expressed with Love"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-05-11-10-GiftsExpressedWithLove.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gifts Expressed with Love"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-05-11-18-GiftsExpressedWithLove.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Prayer"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-05-25-10-Prayer.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Two Questions"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-06-01-10-TwoQuestions.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Order and Authority"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-06-08-10-OrderAndAuthority.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Destiny Rescue"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-06-07-MensBreakfastDestinyRescue.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Resurrection"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-06-15-10-Resurection.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Resurrection"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-06-15-18-Resurection.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Resurrection Body"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-06-22-10-TheResurrectionBody.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Public Prophecy at St Alfred's - Some Guidelines"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-06-18-PublicProphecyAtStAlfreds.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Resurrection Body"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-06-22-18-TheResurrectionBody.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hymns of Praise"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-06-21-HymnsOfPraise.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel Partnerships"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-06-29-10-GospelPartnerships.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Whose Life is it Anyway?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-08-03-10-WhoseLifeIsItAnyway.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel Partnerships"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-06-29-18-GospelPartnerships.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God as Trinity"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-07-06-10-GodAsTrinity.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Trinity and Humanity"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-07-13-18-TrinityAndHumanity.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Trinity and Prayer"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-07-20-10-TrinityAndPrayer.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Trinity and Mission"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-07-27-10-TrinityAndMission.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Relationships to the Glory of God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-08-03-18-RelationshipsToTheGloryOfGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Prayer for Healing"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-08-10-10-PrayerforHealing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Does God Believe in Atheists?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-08-10-18-DoesGodBelieveInAtheists.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: You Can’t Trust the Church Anymore"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-08-17-10-YouCantTrustTheChurchAnymore.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Communion with God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-08-17-18-CommunionWithGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Endless Cycle"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-09-07-10-TheEndlessCycle.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: But who do you say I am?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-08-24-10-ButWhoDoYouSayThatIAm.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Shaky Start"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-08-31-10-AShakyStart.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Asylum Seekers Centre"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-08-30-DavidSpitteler.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Growing food for a hungry planet"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-09-04-GrowingFoodForAHungryPlanet.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Ehud: The Unexpected Rescuer"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-09-14-10-EhudTheUnexpectedRescuer.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Ehud: The Unexpected Rescuer"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-09-14-18-EhudTheUnexpectedRescuer.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Deborah and Barak"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-09-21-10-DeborahAndBarak.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Triumph in Weakness"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-10-05-18-TriumphInWeakness.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Reluctant Leader"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-09-28-10-TheReluctantLeader.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jephthah: A Tragic Outcast"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-10-14-10-JephthahATragicOutcast.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Miracle Birth"
whisper "https://stamp3.s3.amazonaws.com/StAlfreds-2014-10-19-10-AMiracleBirth.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Hidden Epidemic - Depression in Men"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2014-10-18-TheHiddenEpidemic.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Samson: A Man of Passion"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2014-10-28-10-SampsonAManOfPassion.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Suffering Church"
whisper "https://stamp3.s3.amazonaws.com/StAlfreds-2014-11-02-10-TheSufferingChurch.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Samson and Delilah"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2014-11-09-18-SamsonAndDelilah.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Samson and Delilah"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2014-11-09-10-SamsonAndDelilah.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Life with No King"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2014-11-16-18-LifeWithNoKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Council vs. King"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2014-11-16-16-PersistenceUnderPersecution.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: PNG Mission Trip Report"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2014-11-23-18-PNGTeamWhatWeLearntOnOurPNGMissionTripl.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: 10th Anniversary Pulpit Swap"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2014-11-30-10-10thAnniversaryPulpitSwap.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus: The Friend to Everyone"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2014-12-07-10-JesusTheFriendToEveryone.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The God I Don't Understand"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2014-12-14-10-TheGodIDontUnderstand.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Advent and Mission"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2014-12-21-10-AdventAndMission.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christmas Eve 2014"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2014-12-24-2230-ChristmasEve.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Simeon and Anna"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2014-12-28-10-SimeonAndAnna.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Incomparable God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-01-04-10-TheIncomparableGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Complete in Christ"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-01-11-10-CompleteInChrist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Supreme Over All"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-01-18-10-SupremeOverAll.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus Our Rock"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-01-25-10-JesusOurRock.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus Our Fullness"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-02-01-10-JesusOurFullness.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus Our Focus for Life"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-02-08-10-JesusOurFocusforLife.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Chasing Meaning"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-02-08-18-ChasingMeaning.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Marks of True Devotion"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-02-15-10-MarksOfTrueDevotion.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Chasing Fulfilment"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-02-15-18-ChasingFulfilment.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Welcoming the Wanderer"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-02-22-10-WelcomingTheWanderer.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Chasing Time"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-02-22-18-ChasingTime.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Healing and Suffering"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-03-01-10-HealingAndSuffering.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Chasing Justice"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-03-01-18-ChasingJustice.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Stand Firm and Gain Life"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-03-08-10-StandFirmAndGainLife.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Chasing Companionship"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-03-08-18-ChasingCompanionship.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Last Supper"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-03-15-10-TheLastSupper.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Risky Service"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-03-22-10-RiskyService.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Chasing Money"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-03-22-18-ChasingMoney.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Anguish and Betrayal"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-03-29-10-AnguishAndBetrayal.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Chasing God"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-03-15-18-ChasingGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Easter Sunday - Raised"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-04-05-10-EasterSunday-Raised.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Crucified"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-04-03-10-Crucified.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Easter Sunday - Raised"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-04-05-18-Raised.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Risen and Ascended"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-04-12-10-RisenAndAscended.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Risen and Ascended"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-04-12-18-RisenandAscended.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Special People"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-04-19-10-ASpecialPeople.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A New Direction"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-05-03-10-ANewDirection.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: ANZAC Day Centenary"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-04-26-10-ANZACDayCentenary.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A New Identity"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-05-10-18-ANewIdentity.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christians in a hostile world"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-05-17-10-ChristiansInAHostileWorld.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Pentecost Sunday - Prayer for Healing"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-05-24-18-PentecostPrayerforHealing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Pentecost All Age Service 2015"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-05-24-10-Pentecost.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Relationships"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-05-31-10-ChristianRelationships.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Relationships"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-05-31-18-ChristianRelationships.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christians Suffering Persecution"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-06-07-10-ChristiansSufferingPersecution.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Behaviour"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-06-14-10-ChristianBehaviour.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christians Suffering Persecution"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-06-07-18-ChristiansSufferingPersecution.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Suffering and Glory in the World"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-06-21-18-SufferingNGloryInTheWorld.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Everyday Mission"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-07-05-10-EverydayMission.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Suffering and Glory in the Church"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-06-28-10-SufferingAndGloryInTheChurch.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How Should We Pray?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-07-12-18-HowShouldWePray.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Lord if You are Willing"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-07-19-10-LordIfYouAreWilling.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Everyday Mission"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-07-05-18-EverydayMission.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christ's Love Compels Us"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-07-26-10-ChristsLoveCompelsUs.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Pursuing Excellence"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-07-19-18-PursuingExcellence.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Loving Others"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-07-26-18-LovingOthers.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Satisfying the Soul"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-08-02-10-SatisfyingTheSoul.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Radical Power"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-08-02-18-RadicalPower.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Work and Pray"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-08-09-10-WorkAndPray.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Global and Local"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-08-16-10-LocalAndGlobal.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Give and Receive"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-08-23-10-GiveAndReceive.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: All Age Service - August 2015"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-08-30-10-AllAgeService.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Service of Lament"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-08-30-18-AServiceOfLament.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Family Affair"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-09-06-10-AFamilyAffair.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Marriage on the Rocks"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-09-13-10-AMarriageOnTheRocks.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Witness of The Heart"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-09-06-18-TheWitnessoftheHeart.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Love Like the Morning Mist"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-09-20-10-ALoveLikeTheMorningMist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus’ Death & Resurrection"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-09-20-18-Jesus-death-and-resurrection.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus' Words and Deeds"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-09-13-18-Jesus-words-and-deeds.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How Can I Give You Up?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-09-27-10-HowCanIGiveYouUp.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Witness of Scripture"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-09-27-18-TheWitnessOfScripture.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God as Trinity"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-10-04-10-GodAsTrinity.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A People Like the Morning Mist"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-10-11-10-APeopleLikeTheMorningMist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Big Issues - The Environment"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-10-10-BigIssues-TheEnvironment.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Holy Spirit"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-10-11-18-TheHolySpirit.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: I Will Love Them Freely"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-10-18-10-IWillLoveThemFreely.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: From Doubt to Faith"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-10-18-18-FromDoubtToFaith.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Work is a Gift from God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-10-25-10-WorkIsAGiftFromGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Work as Service"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-11-01-10-WorkAsService.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Putting Faith to Work"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-11-08-10-PuttingFaithToWork.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Who Am I?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-11-15-10-WhoAmI.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Breakfast with Bruce Wilson"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-11-14-MensBreakfast-BruceWilson.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Ten things they won't tell you about the New Testament at Uni"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-11-15-18-Ten-things-they-wont-tell-you-about-the-NT-at-uni.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Dwelling Place"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-11-22-18-GodsDwellingPlace.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Fallen King"
whisper "https://stamp3.s3.amazonaws.com/StAlfreds-2015-11-29-10-TheFallenKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Promise of Hope"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-12-06-10-ThePromiseOfHope.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Longed For King"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-12-13-10-TheLongedForKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Foolish King"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-12-20-10-TheFoolishKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The True King"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-12-24-2230-TheTrueKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Eternal King"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-12-27-10-TheEternalKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Chasing Fulfilment"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-02-15-18-ChasingFulfilment.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Welcoming the Wanderer"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-02-22-10-WelcomingTheWanderer.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Chasing Time"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-02-22-18-ChasingTime.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Healing and Suffering"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-03-01-10-HealingAndSuffering.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Chasing Justice"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-03-01-18-ChasingJustice.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Stand Firm and Gain Life"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-03-08-10-StandFirmAndGainLife.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Chasing Companionship"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-03-08-18-ChasingCompanionship.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Last Supper"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-03-15-10-TheLastSupper.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Risky Service"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-03-22-10-RiskyService.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Chasing Money"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-03-22-18-ChasingMoney.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Anguish and Betrayal"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-03-29-10-AnguishAndBetrayal.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Chasing God"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-03-15-18-ChasingGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Easter Sunday - Raised"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-04-05-10-EasterSunday-Raised.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Crucified"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-04-03-10-Crucified.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Easter Sunday - Raised"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-04-05-18-Raised.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Risen and Ascended"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-04-12-10-RisenAndAscended.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Risen and Ascended"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-04-12-18-RisenandAscended.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Special People"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-04-19-10-ASpecialPeople.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A New Direction"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-05-03-10-ANewDirection.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: ANZAC Day Centenary"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-04-26-10-ANZACDayCentenary.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A New Identity"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-05-10-18-ANewIdentity.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christians in a hostile world"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-05-17-10-ChristiansInAHostileWorld.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Pentecost Sunday - Prayer for Healing"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-05-24-18-PentecostPrayerforHealing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Pentecost All Age Service 2015"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-05-24-10-Pentecost.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Relationships"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-05-31-10-ChristianRelationships.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Relationships"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-05-31-18-ChristianRelationships.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christians Suffering Persecution"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-06-07-10-ChristiansSufferingPersecution.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Behaviour"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-06-14-10-ChristianBehaviour.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christians Suffering Persecution"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-06-07-18-ChristiansSufferingPersecution.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Suffering and Glory in the World"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-06-21-18-SufferingNGloryInTheWorld.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Everyday Mission"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-07-05-10-EverydayMission.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Suffering and Glory in the Church"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-06-28-10-SufferingAndGloryInTheChurch.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How Should We Pray?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-07-12-18-HowShouldWePray.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Lord if You are Willing"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-07-19-10-LordIfYouAreWilling.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Everyday Mission"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-07-05-18-EverydayMission.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christ's Love Compels Us"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-07-26-10-ChristsLoveCompelsUs.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Pursuing Excellence"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-07-19-18-PursuingExcellence.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Loving Others"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-07-26-18-LovingOthers.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Satisfying the Soul"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-08-02-10-SatisfyingTheSoul.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Radical Power"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-08-02-18-RadicalPower.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Work and Pray"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-08-09-10-WorkAndPray.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Global and Local"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-08-16-10-LocalAndGlobal.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Give and Receive"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-08-23-10-GiveAndReceive.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: All Age Service - August 2015"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-08-30-10-AllAgeService.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Service of Lament"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-08-30-18-AServiceOfLament.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Family Affair"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-09-06-10-AFamilyAffair.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Marriage on the Rocks"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-09-13-10-AMarriageOnTheRocks.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Witness of The Heart"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-09-06-18-TheWitnessoftheHeart.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Love Like the Morning Mist"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-09-20-10-ALoveLikeTheMorningMist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus’ Death & Resurrection"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-09-20-18-Jesus-death-and-resurrection.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus' Words and Deeds"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-09-13-18-Jesus-words-and-deeds.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How Can I Give You Up?"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-09-27-10-HowCanIGiveYouUp.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Witness of Scripture"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-09-27-18-TheWitnessOfScripture.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God as Trinity"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-10-04-10-GodAsTrinity.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A People Like the Morning Mist"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-10-11-10-APeopleLikeTheMorningMist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Big Issues: The Environment"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-10-10-BigIssues-TheEnvironment.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Holy Spirit"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-10-11-18-TheHolySpirit.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: I Will Love Them Freely"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-10-18-10-IWillLoveThemFreely.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: From Doubt to Faith"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-10-18-18-FromDoubtToFaith.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Work is a Gift from God"
whisper "http://s3-ap-southeast-2.amazonaws.com/stamp3/StAlfreds-2015-10-25-10-WorkIsAGiftFromGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Work as Service"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-11-01-10-WorkAsService.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Putting Faith to Work"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-11-08-10-PuttingFaithToWork.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Who Am I?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-11-15-10-WhoAmI.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Breakfast with Bruce Wilson"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-11-14-MensBreakfast-BruceWilson.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Ten things they won't tell you about the New Testament at Uni"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-11-15-18-Ten-things-they-wont-tell-you-about-the-NT-at-uni.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Dwelling Place"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-11-22-18-GodsDwellingPlace.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Fallen King"
whisper "https://stamp3.s3.amazonaws.com/StAlfreds-2015-11-29-10-TheFallenKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Promise of Hope"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-12-06-10-ThePromiseOfHope.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Longed For King"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-12-13-10-TheLongedForKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Foolish King"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-12-20-10-TheFoolishKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The True King"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-12-24-2230-TheTrueKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Eternal King"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-12-27-10-TheEternalKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Why Don't People Believe"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-01-8-10-WhyDontPeopleBelieve.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Weeds and Yeast"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-01-15-10-WeedsAndYeast.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Treasure and Fish"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-01-22-10-TreasureAndFish.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus Rejected"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-01-29-10-JesusRejected.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: John Beheaded"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-02-05-10-JohnBeheaded.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: 5,000 Fed"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-02-12-10-5000Fed.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Don't be Afraid"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-02-19-18-Don%27t_be_afraid.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Don't Be Afraid"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-02-19-10-DontBeAfraid.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Clean and Unclean"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-02-26-10-CleanAndUnclean.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Do Not Worry"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-03-05-10-AllAgeService.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Great Faith"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-03-05-18-GreatFaith.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: 4,000 Fed"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-03-12-10-4000Fed.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Demand for a Sign"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-03-19-18-DemandForASignt.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Demand For A Sign"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-03-19-10-DemandForASign.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: 4,000 Fed"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-03-12-18-4000-fed.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: You are the Christ"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-03-26-10-YouAreTheChrist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Transfiguration"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-04-02-18-Transfiguration.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Transfiguration"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-04-02-10-Transfiguration.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Healing and Tax"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-04-09-10-HealingAndTax.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Cross and New Life"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-04-14-10-TheCrossAndNewLife.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Breakfast with Ravi Ketharanathan"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-04-01-08-MensBreakfastRaviKetharanathan.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Resurrection of Jesus"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-04-16-10-TheResurrectionOfJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Resurrection of Jesus"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-04-16-18-EasterSunday2017.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Every Blessing"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-04-23-10-EveryBlessing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Thanksgiving And Prayer"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-04-30-10-ThanksGivingAndPrayer.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Grace"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-05-08-18-Grace.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: True Peace"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-05-14-10-TruePeace.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: True Peace"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-05-14-18-TruePeace.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Mission is Messy"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-05-21-10-MissionIsMessy-AllAgeService.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Mystery Revealed!"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-05-21-18-Mystery-revealed.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Love"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-05-28-10-Love.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Love"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-05-28-18-Love.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Mature Christians"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-06-04-10-MatureChristians.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Case For and Against Assisted Suicide: A Medical Perspective"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-06-03-BigIssuesNight-AssistedSuicide-JohnBuchanan.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Case For and Against Assisted Suicide: A Legal & Ethical Perspective"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-06-03-BigIssuesNight-AssistedSuicide-MarkSneddon.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The New You"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-06-11-18-The-New-You.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Godly Life"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-06-18-10-GodlyLife.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Husbands and Wives"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-06-25-10-HusbandsAndWives.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Husbands and Wives"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-06-25-18-HusbandsAndWives.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Home and Work"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2017-07-02-10-HomeAndWork.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Be Strong"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-07-09-18-BeStrong.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Breakfast with Gary Gill - Different Wheels"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-07-15-08-MensBreakfastGaryGillDifferentWheels.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: I'm a Scientist and a Christian - a conversation"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-07-16-18-A-Scientist-and-a-Christian.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Heavens Declare: Science, Faith & the Gospel"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-07-23-10-TheHeavensDeclareScienceFaithandTheGospel.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Heavens Declare: Science, Faith & the Gospel - Q & A"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-07-23-10-TheHeavensDeclareScienceFaithandTheGospel-QandA.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Ministries of Mercy"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-07-30-18-Ministries-of-Mercy.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Reformation of the Bible: William Tyndale"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-08-06-10-AReformationOfTheBibleWilliamTyndale.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Reformation of the Church: Thomas Cranmer"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-08-13-10-ReformationChurchThomasCranmer.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Reformation of the Nation: Elizabeth I"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-08-20-18-ReformationOfTheNationElizabethI.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God Speaks"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2017-08-27-18-God-Speaks.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Ten Commandments"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2017-09-03-10-TenCommandments.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Ten Commandments"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-09-03-18-TenCommandments.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God’s Angel"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-09-10-10-GodsAngel.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Angel"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2017-09-10-18-God%27s-Angel.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Sexuality: Why does it matter who we love?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2017-09-17-18-Sexuality-Why-does-it-matter-who-you-love.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Understanding and Responding to Islam from a Christian Perspective"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-09-17-10-UnderstandingAndRespondingToIslamFromAChristianPerspective.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Assisted Suicide Legislation: Compassion or Abandonment?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-09-24-10-AssistedSuicideLegislation.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gender and Sexuality: Does God's Design Include LGBTI?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2017-09-24-18-Sexuality-Does-Gods-Design-Include-LGBTI.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Sexuality: How Do We Show Grace?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-10-01-18-SexualityHowDoWeShowGrace.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God’s Work Among Iranians"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-10-01-10-InterviewSamFarbod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Covenant"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2017-10-15-18-Covenant.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Covenant"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-10-15-10-Covenant.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Rivers of Justice and Righteousness"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-10-22-10-RiversOfJusticeAndRighteousness.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Rivers of Justice and Righteousness"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-10-22-18-RiversOfJusticeAndRighteousness.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Australians Together"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2017-10-29-18-Australians-Together.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Worship"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2017-11-05-10-Worship.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Golden Calf"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2017-11-12-18-Golden-Calf.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A New Start"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2017-11-19-10-ANewStart.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Breakfast with Tim Budge"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-11-18-08-MensBreakfastTimBudge.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Contend for the Faith"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-11-19-18-%20ContendForTheFaith.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A New Start"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2017-11-26-18-A-New-Start.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Promised King"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2017-12-03-10-ThePromisedKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Mystery of the Kingdom"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2015-12-10-18-TheMysteryOfTheKingdom.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Gospel"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2017-12-10-10-TheGospel.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Promised Place"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2017-12-17-10-ThePromisedPlace.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Promised Saviour"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2017-12-24-10-ThePromisedSaviour.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Promised Son"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2017-12-25-10-ThePromisedSon.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Promised Child"
whisper "https://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2017-12-31-10-ThePromisedChild.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Who is Jesus?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-01-07-18-Who-is-Jesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Promised Gift"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2017-12-24-22-ThePromisedGift.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Who Can Throw the First Stone?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-01-14-10-WhoCanThrowTheFirstStone.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Who Are You?"
whisper "https://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-01-21-18-WhoAreYou.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Who Do You Belong To?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-01-28-10-WhoDoYouBelongTo.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is Jesus Demon-Possessed?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-02-04-18-IsJesusDemonPossessed.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Why is this man blind?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-02-11-10-WhyIsThisManBlind.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Breakfast with Paul Arnott"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-02-10-08-MensBreakfastPaulArnott.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Why is this Man Blind?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-02-11-18-Why-is-this-man-blind.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Do You See?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-02-18-10-DoYouSee.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Do You See?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-02-18-18-DoYouSee.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Who’s Looking After You?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-02-25-10-WhosLookingAfterYou.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Can You Believe in Jesus?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-03-04-18-CanYouBelieveInJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: All Age Service (March 2018)"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-03-04-10-AllAgeService.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: I am the Resurrection and the Life"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-03-11-18-I-am-the-Resurrection-and-the-Life.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: I am the Resurrection and the Life"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-03-11-10-IAmTheResurrectionTheLife.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Prayer and Mission"
whisper "https://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-03-18-10-PrayerAndMission.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Parties and Perfume"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-03-18-18-Parties-and-Perfume.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Cost of Following Jesus"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-03-25-10-TheCostOfFollowingJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Cost of Following Jesus"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-03-26-18-TheCostofFollowingJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good Friday: Death"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-03-30-10-GoodFriday.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Easter Sunday: Life"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-04-01-10-EasterSunday.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Life"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-04-01-18-Life.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Lord and God"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-04-08-10-LordAndGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Follow Me"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-04-15-18-Follow-Me.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Work Matters"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-04-22-10-WorkMatters.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Ambition"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-04-29-18-Ambition.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Ambition"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-04-29-10-Ambition.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Work-Life Balance"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-05-06-10-WorkLifeBalance.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Work-Life Balance"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-05-06-18-WorkLifeBalance.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Thy Kingdom Come"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-05-13-18-ThyKingdomCome.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Prayer for Healing and Faith"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-05-13-10-PrayerForHealingAndFaith.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Prayer Changes Lives"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-05-20-10-ThyKingdomCome.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Thy Kingdom Come (Part 2)"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-05-20-18-ThyKingdomCome2.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: All-Age Service - Love"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-05-27-10-AllAgeServiceLove.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Forgiveness Forsaken or Forgiveness Found"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-05-27-18-Forgiveness-Forsaken-or-Forgiveness-Found.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Breakfast with Paul Omondi from Compassion"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-06-02-08-MensBreakfastPaulOmondi.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Money and Giving"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-06-03-10-MoneyAndGiving.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Volunteering and Retirement"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-06-10-10-VolunteeringRetirement.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Failure and Hope"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-06-10-18-FailureAndHope.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Model Church"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-06-17-18-AModelChurch.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Called to Serve"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-06-24-10-CalledToServe.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Live God's Way"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-07-08-10-LiveGodsWay.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Rapture"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-07-15-18-The-Rapture.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Return of Jesus"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-07-22-10-TheReturnOfJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Return of Jesus"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-07-22-18-The-Return-of-Jesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Stand Firm in Tough Times"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-07-01-18-StandFirmInToughTimes.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Community"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-07-29-10-ChristianCommunity.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Community"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-07-29-18-Christian-Community.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: What if You Lost Everything?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-08-05-18-WorshipWhatIfYouLostEverything.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Meaning"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-08-05-10-Meaning.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Time"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-08-12-10-Time.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: What if You Got Sick?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-08-12-18-What-if-You-Got-Sick.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Cry of Pain"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-08-19-18-ACryOfPain.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Pressure"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-08-19-10-Pressure.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Worship"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-08-26-10-Worship.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Terrifying God and Useless Friends"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-08-26-18-A-Terrifying-God-and-Useless-Friends.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Glimmer of Hope"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-09-02-18-AGlimmerOfHope.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Complete in Christ"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-09-02-10-AndyLittle.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Breakfast with Wei-Han Kuan"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-09-01-08-MensBreakfastWeiHanKuan.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Wealth"
whisper "http://stamp3.s3.amazonaws.com/StLukes-2018-09-09-0930-Wealth.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Where is Wisdom?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-09-09-18-Where-is-Wisdom.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: What's your Question for God?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-09-09-10-FrogOrr-Ewing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Death"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-09-16-10-Death.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Alive in Christ"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-09-17-18-AliveInChrist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God Answers Job"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-09-23-18-God-Answers-Job.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Initiative"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-09-23-10-Initiative.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-09-30-10-God.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: After the Storm"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-09-30-18-After-the-Storm.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Peace"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-10-07-10-Peace.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Hope"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-10-14-10-ChristianHope.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How Green is Our God?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-10-21-10-HowGreenIsOurGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How Green is our God?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-10-21-18-How-Green-is-our-God.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: An Aboriginal Pastor’s Personal Journey"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-10-28-10-AnAboriginalPastorsPersonalJourney.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Morning with Andy Vance"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-11-04-10-AndyVance.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: What Matters: Perseverance"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-11-04-18-What-Matters-Perseverance.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: What Matters: Holiness"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-11-11-18-WhatMattersHoliness.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Foundations for Growth"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-11-18-10-FoundationsForGrowth.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Breakfast with John Steward"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-11-24-08-MensBreakfastJohnSteward.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Living by the Spirit"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-11-25-18-Living-by-the-Spirit.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Surprise, I'm Coming"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-12-02-10-SurpriseImComing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Does God really hear my prayers?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-12-02-18-Does-God-really-hear-my-prayers.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Surprise! The Cost of Christmas"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-12-09-10-SurpriseCostOfChristmas.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Surprise! the Cost of Christmas"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2018-12-09-18-Surprise-The-Cost-of-Christmas.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Surprise! I’ll Be Back"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-12-16-10-SurpriseIllBeBack.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Surprise! Everything Changes"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-12-23-10-SurpriseEverythingChanges.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Surprise! It’s Impossible"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-12-24-2230-SurpriseItsImpossible.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Surprise! I'm Here"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-12-25-10-SurpriseImHere.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2018-12-30-10-GoodNews.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: News Spreads"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-01-06-10-NewsSpreads.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: News Spreads"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-01-06-18-NewsSpreads.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Preaching and Healing"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-01-13-18-PreachingAndHealing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Preaching and Healing"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-01-13-10-PreachingAndHealing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Healing and Forgiveness"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-01-20-18-HealingAndForgiveness.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: New Wineskins"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-01-27-18-New-Wineskins.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Sabbath"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-02-03-10-Sabbath.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Get Connected"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-02-10-10-GetConnected.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Solid Foundations"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-02-17-10-SolidFoundations.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Solid Foundations"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-02-17-18-Solid-Foundations.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Invest Your Life"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-02-24-18-Invest-Your-Life.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Invest Your Life"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-02-24-10-InvestYourLife.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Life of Mission"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-03-03-18-ALifeOfMission.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Life of Mission"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-03-03-10-ALifeOfMission.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Loving God"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-03-10-10-LovingGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Loving God"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-03-10-18-Loving-God.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Crowds and Apostles"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-03-17-10-CrowdsAndApostles.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Crowds and Apostles"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-03-17-18-CrowdsAndApostles.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Misunderstood"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-03-24-10-Misunderstood.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Misunderstood"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-03-24-18-Misunderstood.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Spiritual Gifts"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-03-31-18-SpritualGifts.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: One Spirit, One Body"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-04-07-18-OneSpiritOneBody.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Different Gifts and Roles"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-04-14-10-DifferentGiftsAndRoles.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Different Gifts and Roles"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-04-14-18-Different-Gifts-and-Roles.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Why Does the Resurrection Matter?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-04-21-18-Why-does-the-Resurrection-Matter.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Why Does the Resurrection Matter?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-04-21-10-WhyDoesTheResurrectionMatter.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Why Does the Cross Matter?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-04-19-10-WhyDoesTheCrossMatter.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Power of the Resurrection"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-04-28-10-ThePowerOfTheResurrection.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Power of the Resurrection"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-04-27-19-ThePowerOfTheResurrection.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Power of the Resurrection"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-04-28-18-ThePowerOfTheResurrection.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Character"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-05-05-10-ChristianCharacter.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Character"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-05-05-18-Christian-Character.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Influence"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-05-12-10-ChristianInfluence.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Influence"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-05-12-18-ChristianInfluence.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus and the Old Testament"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-05-19-10-JesusAndTheOldTestament.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus and the Old Testament"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-05-19-18-Jesus-and-the-Old-Testament.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Love Your Enemies"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-05-26-10-LoveYourEnemies.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Brunch with Max Meyers"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-05-25-10-MensBrunchMaxMeyers.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Anger and Lust"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-06-02-18-Anger-and-Lust.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Faithfulness And Integrity"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-06-09-10-FaithfulnessAndIntegrity.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to Give, Pray and Fast"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-06-16-10-HowToGivePrayAndFast.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to Give, Pray and Fast"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-06-16-18-How-to-Give-Pray-and-Fast.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God and Money"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-06-23-10-GodAndMoney.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How To Stop Worrying"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-06-30-10-HowToStopWorrying.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to Stop Worrying"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-06-30-18-How-to-Stop-Worrying.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Your Work and God's Work"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-07-07-18-YourWorkAndGodsWork.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Your Work as a Missionfield"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-07-07-10-YourWorkAsAMissionfield.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Building a Secure Future"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-07-14-18-BuildingASecureFuture.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Do Unto Others"
whisper "http://stamp3.s3.amazonaws.com/StLukes-2019-07-07-0930-DoUntoOthers.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is God Good?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-07-21-10-IsGodGood.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is God Generous?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-08-04-10-IsGodGenerous.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is God Liberating?"
whisper "http://s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-08-11-10-IsGodLiberating.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is God Fulfilling?"
whisper "http://s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-08-18-10-IsGodFulfilling.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is God Fulfilling?"
whisper "http://s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-08-18-18-Is-God-Fulfilling.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is God Life-Giving?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-08-25-10-IsGodLifeGiving.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is God Joyful?"
whisper "http://s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-09-01-10-IsGodJoyful.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Who Can You Trust"
whisper "http://s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-09-08-10-WhoCanYouTrust.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Who Can You Trust"
whisper "http://s3.amazonaws.com/StAlfreds-2019-09-08-18-WhoCanYouTrust.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Confident in Christ"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-09-15-10-ConfidentInChrist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Living in Christ"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-09-22-10-LivingInChrist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Living in Christ"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-09-22-18-LivingInChrist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: One In Christ"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-09-29-10-OneInChrist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Brunch with Tom and Caleb Lobbe"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-09-14-10-MensBrunchTomAndCalebLobbe.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: One in Christ"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-09-29-18-One-in-Christ.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Obedient in Christ"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-10-06-10-ObedientInChrist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Obedient in Christ"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-10-06-18-ObedientInChrist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Resurrection and Suffering"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-10-13-10-ResurrectionandSuffering.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Righteous in Christ"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-10-13-18-Righteous-in-Christ.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Transformed in Christ"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-10-20-10-TransformedInChrist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: All Age Service"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-10-27-10-AllAgeService.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Content in Christ"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-11-03-10-ContentInChrist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Crazy Busy"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-11-10-10-CrazyBusy.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Shape of Discipleship"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-11-10-18-The-Shape-of-Discipleship.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Justice"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-11-17-18-Justice.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Cry for Justice"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-11-17-10-CryForJustice.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Helping the Needy"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-11-24-18-Helping-the-Needy.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus on Justice"
whisper "http://stamp3.s3.amazonaws.com/StLukes-2019-11-24-0930-JesusOnJustice.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Brunch with Craig, Carlo, Dave, Doug & Andrew"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-11-23-10-MensBrunchCraigCarloDaveDougAndrew.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is Christmas Believable?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-12-01-18-Is-Christmas-Believable.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is Christmas Divisive?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2019-12-08-10--IsChristmasDivisive.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Service of Comfort"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-12-10-1430-ServiceOfComfort.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is Christmas Believable?"
whisper "http://stamp3.s3.amazonaws.com/StLukes-2019-12-01-0930-IsChristmasBelievable.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is Christmas Divisive?"
whisper "http://stamp3.s3.amazonaws.com/StLukes-2019-12-08-0930-IsChristmasDivisive.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is Christmas Just For Kids?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-12-15-10-IsChristmasJustForKids.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is Christmas Just For Kids?"
whisper "http://stamp3.s3.amazonaws.com/StLukes-2019-12-15-0930-IsChristmasJustForKids.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is Christmas for Me?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-12-22-10-IsChristmasForMe.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is Christmas for Me?"
whisper "http://stamp3.s3.amazonaws.com/StLukes-2019-12-22-0930-IsChristmasForMe.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is Christmas Essential?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-12-24-2230-IsChristmasEssential.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is Christmas Joyful?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-12-25-10-IsChristmasJoyful.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is Christmas Sustainable?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2019-12-29-10-IsChristmasSustainable.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is Christmas Joyful?"
whisper "http://stamp3.s3.amazonaws.com/StLukes-2019-12-25-0930-IsChristmasJoyful.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Kingdom in Danger"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2020-01-05-18-The-Kingdom-in-Danger.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Solomon's Rule"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2020-01-12-18-Solomons-Rule.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Solomon's Rule"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2020-01-12-10-SolomonsRule.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Solomon’s Wisdom"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2020-01-19-10-SolomonsWisdom.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Solomon's Wisdom"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-01-19-18-SolomonsWisdom.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jordan Hitchcock - Farewell"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2020-01-26-10-JordanHitchcockFarewell.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Wisdom in Action"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2020-02-02-10-WisdomInAction.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Temple of the Lord"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2020-02-09-10-TheTempleOfTheLord.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The God of Heaven & Earth: Prayer for Healing"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-02-16-10-TheGodOfHeavenAndEarth-PrayerForHealing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The God of Heaven & Earth"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-02-16-18-TheGodOfHeavenAndEarth.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God Speaks"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-02-23-10-GodSpeaks.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's & Women's Grill with Greg Sheridan - Introduction"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-02-22-1800-MensAndWomensGrill-GregSheridan-IsGodForYou.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's & Women's Grill with Greg Sheridan - Is God Good for You?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-02-22-1805-MensAndWomensGrill-GregSheridan-IsGodForYou.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's and Women's Grill with Greg Sheridan - Interview"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-02-22-1830-MensAndWomensGrill-GregSheridan-IsGodForYou.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's and Women's Grill with Greg Sheridan - Q & A"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-02-22-1900-MensAndWomensGrill-GregSheridan-IsGodForYou.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Wisdom and Wealth"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2020-03-01-18-WisdomAndWealth.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Kingdom in Danger"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StLukes-2020-01-05-0930-TheKingdomInDanger.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Solomon’s Rule"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StLukes-2020-01-12-0930-SolomonsRule.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Wisdom in Action"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StLukes-2020-02-02-0930-WisdominAction.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Temple of the Lord"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StLukes-2020-02-09-0930-TheTempleOfTheLord.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The God of Heaven and Earth"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StLukes-2020-02-16-0930-GodOfHeavenAndEarth.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God Speaks"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StLukes-2020-02-23-0930-GodSpeaks.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Wisdom and Wealth"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StLukes-2020-03-01-0930-WisdomandWealth.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Divided King, Divided Kingdom"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2020-03-08-18-Divided-King-Divided-Kingdom.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Simeon"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2020-03-15-10-Simeon.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men’s Event - Following Jesus in All We Do Living in an Age of Pornography"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-03-16-1945-MensEvent-FollowingJesusInAllWeDoLivingInAnAgeOfPornography.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Anna"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2020-03-22-10-Anna.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Faith In A Time Of Fear"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-03-29-10-FaithInTimeOfFear.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Don't Waste Your Discomfort"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-04-05-10-DontWasteYourDiscomfort.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good Friday 2020"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-04-10-10-GoodFriday.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Easter Sunday 2020"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-04-12-10-EasterSunday.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to be a Spiritual Survivor"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-04-19-10-HowToBeASpiritualSurvivor.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: John"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-04-26-10-John.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Family"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-05-03-10-Family.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Temptation"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-05-10-10-Temptation.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Nazareth"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-05-17-10-Nazareth.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Authority"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-05-24-10-Authority.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Pentecost"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-05-31-10-Pentecost.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Healing"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-06-07-10-Healing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Fishing"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-06-14-10-Fishing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Leprosy"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-06-21-10-Leprosy.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Forgiveness"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-06-28-10-Forgiveness.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Levi"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-07-05-10-Levi.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Wine"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-07-12-10-Wine.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Sabbath"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-07-19-10-Sabbath.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Everything's Changed But God is Still in Charge"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-07-26-10-EverythingsChangedButGodIsStillInCharge.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Prayer and Lament"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-08-02-10-PrayerAndLament.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Why Would a Loving God Allow a Pandemic to Happen?"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-08-09-10-WhyWouldALovingGodAllowAPandemicToHappen.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Crisis is an Opportunity for Spiritual Growth"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-08-16-10-CrisisIsAnOpportunityForSpiritualGrowth.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hope, Love and Good Works in a Time of Danger"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-08-23-10-HopeLoveAndGoodWorksInATimeOfDanger.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Thank God for All of You"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-08-30-10-ThankGodForAllOfYou.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The God of All Comfort"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-09-06-10-TheGodOfAllComfort.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Zoom Men’s Event - Navigating the Seasons of a Man's Life"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2020-09-05-17-MensEvent-NavigatingTheSeasonsOfAMansLife.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Lord is Close"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-09-13-10-TheLordIsClose.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God’s Word Strengthens Us"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-09-20-10-GodsWordStrengthensUs.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God Goes With You"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-09-27-10-GodGoesWithYou.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Rest for the Soul"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-10-04-10-RestFGorTheSoul.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How To Know God"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-10-25-10-HowToKnowGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to Be a Genuine Christian"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-11-01-10-HowToBeAGenuineChristian.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to Stay the Course"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-11-08-10-HowToStayTheCourse.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to Be a Child of God"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-11-15-10-HowToBeAChild%20of%20God.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Zoom Men’s Event - Broken in Body, Booming in the Spirit"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2020-11-14-17-MensEvent-BrokenInBodyBoomingInTheSpirit.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Zoom Men’s Event - Broken in Body, Booming in the Spirit - Q and A"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2020-11-14-17-MensEvent-BrokenInBodyBoomingInTheSpirit-QA.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Devotional Talk On Psalm 103"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2020-11-22-10-DevotionalTalkOnPsalm103.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: O Come, O Come Emmanuel"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-11-29-10-OComeOComeEmmanuel.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: His Name is Wonderful"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-12-06-10-HisNameIsWonderful.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Lion and The Lamb"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-12-20-10-TheLionAndTheLamb.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Darkness and Light"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2020-12-24-2230-DarknessAndLight.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Light of the World"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2020-12-25-10-LightOfTheWorld.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: 'Next Day' Spirituality"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2020-12-27-10-NextDaySpirituality.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to Show Love"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-01-03-00-HowToShowLove.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to Know God Loves You"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-01-10-00-HowToKnowGodLovesYou.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How to be Sure of Your Faith"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-01-17-00-HowToBeSureOfYourFaith.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Truth Love and Faith"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-01-24-00-TruthLoveAndFaith.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good and Bad Leaders"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-01-31-00-GoodAndBadLeaders.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good and Bad Leaders"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-01-31-10-GoodAndBadLeaders.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Lost Son"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-01-24-18-TheLostSon.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Shrewd Manager"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-01-31-18-TheShrewdManager.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Lord Ascends"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-02-07-00-TheLordAscends.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A New Apostle"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-02-14-00-ANewApostle.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Filled With The Holy Spirit"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-02-21-00-FilledWithTheHolySpirit.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus Is Lord"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-02-28-00-JesusIsLord.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Church Begins"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-03-07-00-TheChurchBegins.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Healing in Jesus' Name"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-03-14-00-HealingInJesusName.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Prophets Point to Jesus"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-03-21-00-TheProphetsPointToJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: No Other Name"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-03-28-00-NoOtherName.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: No Other Name"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-03-28-18-No-Other-Name.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hope"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-04-02-00-Hope.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Resurrection Hope"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-04-04-00-ResurrectionHope.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Resurrection Hope"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-04-04-10-ResurrectionHope.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Resurrection Hope"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-04-04-18-ResurrectionHope.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Prayer for Boldness & Miracles"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-04-11-00-PrayerForBoldnessAndMiracles.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: One In Heart & Mind"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-04-18-00-OneInHeartAndMind.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Ananias and Sapphira"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-04-25-00-AnaniasAndSapphira.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Healing, Signs and Wonders"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-05-02-00-HealingSignsAndWonders.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Ananias and Sapphira"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-04-25-10-AnaniasAndSapphira.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Rejoicing Under Persecution"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-05-09-00-RejoicingUnderPersecution.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Rejoicing Under Persecution"
whisper "http://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2021-05-09-18-RejoicingUnderPersecution.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Stephen"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-05-16-00-Stephen.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Stephen"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-05-16-18-Stephen.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A History of Human Rebellion"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-05-23-00-AHistoryOfHumanRebellion.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A History of Human Rebellion"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-05-23-18-AHistoryOfHumanRebellion.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Gospel Spreads Due to Persecution"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-05-30-00-TheGospelSpreadsDueToPersecution.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Mission in the Northern Territory"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-06-06-00-MissionInTheNorthernTerritory.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Mission in Samaria"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-06-13-00-MissionInSamaria.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Philip & an Ethiopian Seeker"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-06-20-00-PhilipAndAnEthiopianSeeker.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Saul's Conversion"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-06-27-00-SaulsConversion.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Saul in Jerusalem"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-07-04-00-SaulInJerusalem.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Tabitha Raised from the Dead"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-07-11-00-TabithaRaisedFromTheDead.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Peter's Vision"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-07-18-00-PetersVision.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Gospel Spreads"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-07-25-00-TheGospelSpreads.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Peter Explains His Vision"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-08-01-00-PeterExplainsHisVision.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Peter Explains His Vision"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-08-01-18-PeterExplainsHisVision.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Barnabas & Saul in Antioch"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-08-08-00-BarnabasAndSaulInAntioch.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Peter Escapes"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-08-15-00-PeterEscapes.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Royal Family"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-08-22-00-ARoyalFamily.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Miss Universe Is Crowned"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-08-29-00-MissUniverseIsCrowned.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Threat Of Genocide"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-09-05-00-TheThreatOfGenocide.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Defining Moment"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-09-12-00-ADefiningMoment.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Honoured & Humbled"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-09-19-00-HonouredAndHumbled.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Deliverance"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-09-26-00-Deliverance.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How Your Story Connects With God's Story"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-10-03-00-HowYourStoryConnectsWithGodsStory.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Persistent Prayer"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-10-10-00-PersistentPrayer.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Godly Wisdom From God's Word"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-10-17-00-GodlyWisdomFromGodsWord.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Accountability"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-10-24-00-Accountability.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Connecting To God In Worship"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-10-31-00-ConnectingToGodInWorship.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Serving Others"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-11-07-00-ServingOthers.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Generosity"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-11-14-00-Generosity.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Generosity"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-11-14-10-Generosity.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Event - Releasing The Underground Forest"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-11-13-17-MensEvent-ReleasingTheUndergroundForest.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Event - Releasing The Underground Forest - Q&A"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-11-13-17-MensEvent-ReleasingTheUndergroundForest-Q_A.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Promoting The Gospel"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-11-21-00-PromoningTheGospel.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Peace and Hope"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-11-28-00-PeaceAndHope.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Promoting the Gospel"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-11-21-10-PromoningTheGospel.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Living Now, Looking Forward"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-12-05-00-LivingNowLookingForward.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Living Now, Looking Forward"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-12-05-10-LivingNowLookingForward.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Firm To The End"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-12-12-00-FirmToTheEnd.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Firm To The End"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-12-12-18-FirmToTheEnd.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Waiting And Praying"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-12-19-00-WaitingAndPraying.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hope In The Darkness"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-12-24-2230-HopeInTheDarkness.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hope Revealed"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-12-25-10-HopeRevealed.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Known By God, Comfort In Distress"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2021-12-26-00-KnownByGodComfortInDistress.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Give Thanks"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-01-02-00-GiveThanks.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: No Fear of Bad News"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-01-02-10-NoFearOfBadNews.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Perfect King"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-01-02-18-ThePerfectKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Incomparable God"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-01-09-00-TheIncomparableGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Psalm 145"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-01-16-00-Psalm145.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Psalm 100"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-01-16-18-Psalm100.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Wisdom and Guidance"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-01-23-00-WisdomAndGuidance.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Greatness of God"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-01-23-10-TheGreatnessOfGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Word of God"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-01-23-18-TheWordOfGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Be My Rock"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-01-30-00-BeMyRock.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Be My Rock"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-01-30-18-BeMyRock.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Honourable Servant"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-02-06-00-TheHonourableServant.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Be Strong & Courageous"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-02-13-00-BeStrongAndCourageous.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Rahab The Prostitute"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-02-20-00-RahabTheProstitute.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Loving Jesus Means Heeding Jesus"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-02-06-18-LovingJesusMeansHeedingJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Crossing The Jordan"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-02-27-00-CrossingTheJordan.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Crossing The Jordan"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-02-27-18-CrossingTheJordan.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jericho"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-03-06-00-Jericho.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Covenant"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-03-13-00-Covenant.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Killing Canaanites: The Issue of War in Joshua"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-03-16-1930-KillingCanaanitesSeminar.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Conquest"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-03-20-00-Conquest.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Promised Land"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-03-27-00-ThePromisedLand.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Conquest"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-03-20-18-Conquest.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Covenant"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-03-13-18-Covenant.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jericho"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-03-06-10-Jericho.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jericho"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-03-06-18-Jericho.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hold Fast To The Lord"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-04-03-00-HoldFastToTheLord.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hold Fast To The Lord"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-04-03-10-HoldFastToTheLord.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Serve The Lord"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-04-10-00-ServeTheLord.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Serve The Lord"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-04-10-10-ServeTheLord.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Witness His Resurrection"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-04-17-10-WitnessHisResurrection.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Witness His Resurrection"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-04-17-18-WitnessHisResurrection.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Witness His Death"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-04-15-10-WitnessHisDeath.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hope For Ukraine"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-04-24-10-HopeForUkraine.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Event - Life Lessons From Vietnam"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-04-30-10-MensEvent-VietnamWarTalk.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Testing of Abraham"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-05-01-10-TheTestingOfAbraham.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Use Your Gifts"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-05-08-10-UseYourGifts.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Don't Be Ashamed"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-05-15-10-DontBeAshamed.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Be Strong in Christ"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-05-22-10-BeStrongInChrist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Godly Disputes"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-05-29-10-GodlyDisputes.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Godly Disputes"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-05-29-18-GodlyDisputes.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God's Global Gospel Strategy"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-06-05-10-GodsGlobalGospelStrategy.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Spirit of Power and Love"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-06-05-18-ASpiritOfPowerAndLove.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Call to Mission"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-06-12-10-ChristianCallToMission.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Dangerous Days"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-06-19-10-DangerousDays.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Dangerous Days"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-06-19-18-DangerousDays.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Keep Going"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-06-26-18-KeepGoing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Keep The Faith"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-07-03-10-KeepTheFaith.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Safe With The Lord"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-07-10-18-SafeWithTheLord.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Christian Call to Mission"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-07-17-18-ChristianCallToMission.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Forest Underground"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-07-24-10-TheForestUnderground.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Forest Underground"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-07-24-18-TheForestUnderground.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How Long, O Lord?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-07-31-10-HowLongOLord.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Who Am I and Who Do I Love?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-07-31-18-WhoAmIAndWhoDoILove.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: You Can’t Be Serious, O Lord!"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-08-07-10-YouCantBeSeriousOLord.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God’s Good Design and the Mistakes We Make"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-08-07-18-GodsGoodDesignAndTheMistakesWeMake.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Is Following Jesus Worth It?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-08-14-18-IsFollowingJesusWorthIt.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: I Stand in Awe, O Lord"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-08-14-10-IStandInAweOLord.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Love in the Time of Climate Change"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-08-21-10-LoveInTheTimeOfClimateChange.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Creation"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-08-28-10-Creation.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Two Books of God: The Bible and the Creation"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-09-04-10-TheTwoBooksOfGodTheBibleAndTheCreation.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Creation Peopled"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-09-11-10-CreationPeopled.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Creation and Evolution: Two Sides of the Same Coin?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-09-18-10-CreationAndEvolutionTwoSidesOfTheSameCoin.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Creation Ruined"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-09-25-10-CreationRuined.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Creation Care: Why Bother?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-10-02-10-CreationCareWhyBother.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Creation Redeemed"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-10-09-10-CreationRedeemed.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Creation Transformed"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-10-23-10-CreationTransformed.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Transhumanism: Fulfilling or Forsaking the Call of Christ?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-10-30-10-TranshumanismFulfillingOrForsakingTheCallOfChrist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Born to Set an Example"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-11-27-18-BornToSetAnExample.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Born to Create a United People"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-12-04-18-BornToCreateAUnitedPeople.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Born to Reshape Our Lives"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-12-11-10-BornToReshapeOurLives.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Born to Conquer Evil"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-12-18-10-BornToConquerEvil.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Born as God in a Manger"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-12-24-2230-BornAsGodInAManger.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Born So We Might Shine Like Stars"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2022-12-25-10-BornSoWeMightShineLikeStars.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: My Eyes Have Seen"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-01-01-10-MyEyesHaveSeen.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Blessing & Deception"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-01-08-10-BlessingAndDeception.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Blessing & Honesty"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-01-15-10-BlessingAndHonesty.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Blessing & Wisdom"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-01-22-10-BlessingAndWisdom.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Blessing & Peace"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-01-29-10-BlessingAndPeace.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Blessing & Suffering"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StLukes-2023-02-05-0930-Blessingandsuffering.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Living For Christ"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-02-05-10-LivingForChrist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Living For Christ"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-02-05-18-LivingForChrist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Blessing & Prosperity"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-02-12-10-BlessingAndProsperity.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Be a Blessing"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-02-19-18-BeABlessing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Greatness and Humility"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-02-26-10-GreatnessAndHumility.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Restoration and Prayer"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-03-05-10-RestorationAndPrayer.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Mercy and Forgiveness"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-03-12-10-MercyAndForgiveness.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Marriage and Children"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-03-19-10-MarriageAndChildren.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Cost and Reward"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-03-26-10-CostAndReward.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus Enters Jerusalem"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-04-02-10-JesusEntersJerusalem.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Cross of Jesus"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-04-07-10-The%20CrossOfJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Resurrection of Jesus"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-04-09-10-TheResurrectionOfJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Grace and Grumbling"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-04-16-10-GraceAndGrumbling.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Suffering and Death"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-04-23-10-SufferingAndDeath.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Compassion and Healing"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-04-30-10-CompassionAndHealing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Off to a Bad Start"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-05-07-10-OffToABadStart.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Keep God’s Commands"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-05-14-10-KeepGodsCommands.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Event - Life and Faith Challenges"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StLukes-2023-05-13-10-MensEvent-LifeAndFaithChallenges.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Event - When God Goes To Work"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-02-11-17-MensEvent-WhenGodGoesToWork.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Event - When God Goes To Work - Q&A"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-02-11-17-MensEvent-WhenGodGoesToWorkQA.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Commandments 1-3"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-05-21-10-Commandments1_3.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God Sends His Spirit"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-05-28-10-GodSendsHisSpirit.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Commandments 4-10"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-06-04-10-Commandments4-10.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Love the Lord Your God"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-06-11-10-LoveTheLordYourGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: You are Precious"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-06-18-10-YouArePrecious.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Don’t Let Wealth Be Your God"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-06-25-10-DontLetWealthBeYourGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Spiritual Gifts with Humility"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-07-02-10-SpiritualGiftsWithHumility.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Spiritual Gifts with Unity"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-07-09-18-SpiritualGiftsWithUnity.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Power Of Spiritual Gifts"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-07-16-10-ThePowerOfSpiritualGifts.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Power Of God"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-07-16-18-ThePowerOfGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Spiritual Gifts for Service"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-07-23-10-SpiritualGiftsForService.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Ken Fish - Healing"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-07-14-1900-KenFishHealing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Ken Fish - Evangelism and Spiritual Gifts 1"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-07-15-1030-KenFishEvangelismAndSpiritualGifts.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Ken Fish - Evangelism and Spiritual Gifts 2"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-07-15-1400-KenFishEvangelismAndSpiritualGifts.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Ken Fish - Evangelism and Spiritual Gifts 3"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-07-15-1900-KenFishEvangelismAndSpiritualGifts.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Golden Calf"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-07-30-10-TheGoldenCalf.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Who Is This God?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-08-06-10-WhoIsThisGod.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: You Choose: Blessing or Curse?"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-08-13-10-YouChooseBlessingOrCurse.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Mission in Word, Spirit & Deed"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-09-03-10-MissionInWordSpiritAndDeed.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Suffering and Comfort"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-09-10-10-SufferingAndComfort.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: When Trust is Threatened"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-09-17-10-WhenTrustIsThreatened.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Gospel of Christ"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-09-24-10-TheGospelOfChrist.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel Glory"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-10-01-10-GospelGlory.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Preach Jesus Christ as Lord"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-10-08-10-PreachJesusChristAsLord.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Our Eternal Home"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-10-15-10-OurEternalHome.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Our Eternal Home"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-10-15-18-OurEternalHome.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel Generosity"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-10-29-10-GospelGenerosity.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Joy and Sorrow"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-11-12-10-JoyAndSorrow.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Open Wide Your Hearts"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-11-05-18-OpenWideYourHearts.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Called to Serve"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-11-19-10-CalledToServe.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Called to Serve"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-11-19-18-CalledToServe.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: We Want a King"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-11-26-18-WeWantAKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Saul: The People’s Choice of King"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-12-03-10-SaulThePeoplesChoiceOfKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: David: God’s Choice of King"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-12-10-10-DavidGodsChoiceOfKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: David: God’s Choice of King"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-12-10-18-DavidGodsChoiceOfKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Manasseh: The Worst King"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-12-17-10-ManassehTheWorstKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The King is Born"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-12-24-2230-TheKingIsBorn.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Jesus, The King"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-12-25-10-JesusTheKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Long-Awaited King"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2023-12-31-10-TheLongAwaitedKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Envy & Contentment"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-01-07-10-EnvyAndContentment.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gluttony & Self-Control"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-01-14-10-GluttonyAndSelfControl.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Sloth & Diligence"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-01-21-10-SlothAndDilegence.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Greed & Generosity"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-01-28-10-GreedAndGenerosity.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Wrath & Reconciliation"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-02-04-10-WrathAndReconciliation.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Pride & Humility"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-02-11-10-PrideAndHumility.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Life and Death"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-02-18-10-LifeAndDeath.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Feet Anointed"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-02-25-10-FeetAnointed.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Hour Has Come"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-03-03-10-TheHourHasCome.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Belief and Unbelief"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-03-10-10-BeliefAndUnbelief.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Feet Washed"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-03-17-10-FeetWashed.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Love and Betrayal"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-03-24-10-LoveAndBetrayal.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Love and Betrayal"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-03-24-18-LoveAndBetrayal.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Death"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-03-29-10-Death.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Life"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-03-31-10-Life.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Life"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-03-31-18-Life.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Withstanding Personal Attack"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-04-14-10-WithstandingPersonalAttack.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Giving Cheerfully and Generously"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-04-07-10-GivingCheerfullyAndGenerously.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: True and False Ministers"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-04-21-10-TrueAndFalseMinisters.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: The Cost of Ministry"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-04-28-10-TheCostOfMinistry.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Strength in Weakness"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-05-05-10-StrengthInWeakness.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Warning and Encouragement"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-05-12-10-WarningAndEncouragement.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Judgment and Hope"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-05-26-10-JudgmentAndHope.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A New Order"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-05-19-10-ANewOrder.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Holy King"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-06-02-10-AHolyKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: A Foolish King"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-06-09-10-AFoolishKing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Misplaced Trust"
whisper "http://stamp3.s3-ap-southeast-2.amazonaws.com/StAlfreds-2024-06-16-10-MisplacedTrust.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God Can Save Zion"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-06-23-10-GodCanSaveZion.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Comfort, Comfort"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-06-30-10-ComfortComfort.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: God’s Servant Will Rescue"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-07-07-10-GodsServantWillRescue.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Come Thou Long Expected Jesus"
whisper "http://stamp3.s3.amazonaws.com/StAlfreds-2020-12-13-10-ComeThouLongExpectedJesus.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: All Things New"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-07-14-18-AllThingsNew.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News in Hands, Feet, and Speech"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-07-21-10-GoodNewsInHandsFeetAndSpeech.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News in Hands, Feet, and Speech"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-07-21-18-GoodNewsInHandsFeetAndSpeech.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News for All - Without Conditions"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-07-28-10-GoodNewsForAllWithoutConditions.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News vs Superstitions"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-08-04-10-GoodNewsVsSuperstitions.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News vs Idolatry and Philosophy"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-08-11-10-GoodNewsVsIdolatryAndPhilosophy.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News vs Idolatry and Philosophy"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-08-11-18-GoodNewsVsIdolatryAndPhilosophy.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Growing in the Word and Spirit"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-08-18-10-GoodNewsVsSpiritualForces.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News vs Spiritual Forces"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-08-18-18-GoodNewsVsSpiritualForces.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News-shaped Messengers"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-08-18-25-GoodNewsShapedMessengers.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News on Trial"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-09-01-10-GoodNewsOnTrial.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News on Trial"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-09-01-18-GoodNewsOnTrial.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News in the Midst of Storms"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-09-08-10-GoodNewsInTheMidstOfStorms.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News in the Midst of Storms"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-09-08-18-GoodNewsInTheMidstOfStorms.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Singing: To God and One Another"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-09-15-10-SingingToGodAndOneAnother.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Scripture: Read and Taught"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-09-22-10-ScriptureReadAndTaught.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Supplication: In Confession and Prayer"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-09-29-10-SupplicationInConfessionAndPrayer.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Unity Leading to Mission"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-10-06-10-UnityLeadingToMission.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Sacrament: Grace Revealed and Received"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-10-13-10-SacramentGraceRevealedAndReceived.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Sacrament: Grace Revealed and Received"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-10-13-18-SacramentGraceRevealedAndReceived.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Spirit: Edification & Empowerment"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-10-20-10-SpiritEdificationAndEmpowerment.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Spirit: Edification & Empowerment"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-10-20-18-SpiritEdificationAndEmpowerment.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Sent: In Love and Service"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-10-27-10-SentInLoveAndService.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Growing in Godliness"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-11-03-10-GrowingInGodliness.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Growing in Discernment"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-11-10-10-GrowingInDiscernment.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Growing in Truth"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-11-10-18-GrowingInTruth.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Growing in Discernment"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-11-17-18-GrowingInDiscernment.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Growing in Hope"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-11-24-10-GrowingInHope.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Advent Hope"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-12-01-10-AdventHope.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Advent Peace"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-12-08-10-AdventPeace.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Advent Love"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-12-15-10-AdventLove.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Advent Joy"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-12-22-10-AdventJoy.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Rejoice in God’s Salvation"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-12-24-2230-RejoiceInGodsSalvation.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good News of Great Joy"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-12-25-10-GoodNewsOfGreatJoy.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: How We Can Grow"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2024-12-29-10-HowWeCanGrow.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Wisdom that Helps Us"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-01-05-10-WisdomThatHelpsUs.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Guard Your Heart"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-01-12-10-GuardYourHeart.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Purity and Faithfulness"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-01-19-10-PurityAndFaithfulness.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Wisdom at Work"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-01-26-10-WisdomAtWork.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel-Shaped Priorities"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-02-02-10-GospelShapedPriorities.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel-Shaped Expectations"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-02-09-10-GospelShapedExpectations.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel-Shaped Sacrifice"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-02-16-10-GospelShapedSacrifice.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel-Shaped Teamwork"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-02-23-10-GospelShapedTeamwork.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel-Shaped Love"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-03-02-10-GospelShapedLove.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel-Shaped Resilience"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-03-09-10-GospelShapedResilience.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel-Shaped Work & Worship"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-03-16-10-GospelShapedWorkAndWorship.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel-Shaped Work & Worship"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-03-16-18-GospelShapedWorkAndWorship.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel-Shaped Prayer"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-03-23-10-GospelShapedPrayer.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel-Shaped Hospitality"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-03-30-10-GospelShapedHospitality.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel-Shaped Rejoicing"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-04-06-10-GospelShapedRejoicing.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel-Shaped Decisions"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-04-13-10-GospelShapedDecisions.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel-Shaped Decisions"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-04-13-18-GospelShapedDecisions.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel-Shaped Hospitality"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-03-30-18-GospelShapedHospitality.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Good Friday: BROKEN"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-04-18-10-GoodFridayBroken.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Easter Sunday: RESTORED"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-04-20-10-EasterSundayRestored.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hope In Suffering"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-04-27-10-HopeInSuffering.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hope When We Feel Hopeless"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-05-04-10-HopeWhenWeFeelHopeless.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hope For The Future"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-05-11-10-HopeForTheFuture.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Gospel-Shaped Sacrifice"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-02-16-18-GospelShapedSacrifice.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hope for Justice"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-05-18-10-HopeForJustice.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hope for Authentic Living"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-05-25-10-HopeForAuthenticLiving.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Hope in an Age of Science"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-06-01-10-HopeInAnAgeOfScience.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Pentecost 2025"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-06-08-18-Pentecost.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Maturity in Trials"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-06-15-10-MaturityInTrials.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Maturity in Mercy"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-06-29-10-MaturityInMercy.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Maturity in Obedience"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-06-22-10-MaturityInObedience.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Men's Event - Servant or Saviour? AI and Techno-Utopianism"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-06-28-10-MensEvent-ServantOrSaviourAIAndTechnoUtopianism.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Maturity in Action"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-07-06-10-MaturityInAction.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Maturity in Speech"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-07-13-10-MaturityInSpeech.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Maturity in Wisdom"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-07-20-18-MaturityInWisdom.mp3" --model medium --output_dir "transcripts" --language English

echo "Transcribing: Maturity in Conflict"
whisper "https://stamp3.s3.ap-southeast-2.amazonaws.com/StAlfreds-2025-07-27-10-MaturityInConflict.mp3" --model medium --output_dir "transcripts" --language English

