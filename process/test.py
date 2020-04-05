import twint

c = twint.Config()
#c.Username = "@KieuTien278"
c.Search = "covid"
#c.Limit = 500
c.Since = "2020-03-20"
#c.Until = "2020-03-10"
#c.User_full = True
c.Lang = "vi"
c.Store_csv = True
c.Output = "vienamcovid.csv"
#twint.run.Lookup(c)
twint.run.Search(c)
