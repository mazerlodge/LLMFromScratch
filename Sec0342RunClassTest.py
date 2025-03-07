from Sec0342SelfAttentionClass import SelfAttention_v1 

torch.manual_seed(123)
sa_v1 = SelfAttention_v1(d_in, d_out)
print(sa_v1(inputs))