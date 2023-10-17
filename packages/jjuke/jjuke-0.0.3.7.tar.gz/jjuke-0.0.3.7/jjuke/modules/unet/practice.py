class LinearAttention2D(nn.Module):
    def __init__(self, dim, heads = 4, dim_head = 32):
        super().__init__()

        self.scale = dim_head ** -0.5
        self.heads = heads
        hidden_dim = dim_head * heads

        self.norm = LayerNorm(2, dim)
        self.to_qkv = conv_nd(2, dim, hidden_dim*3, 1, bias=False)
        self.to_out = nn.Sequential(
            conv_nd(2, hidden_dim, dim, 1),
            LayerNorm(2, dim)
        )

    def forward(self, x):
        b, c, h, w = x.shape

        x = self.norm(x) # for 2D U-Net
        
        qkv = self.to_qkv(x).chunk(3, dim = 1)
        q, k, v = map(lambda t: rearrange(t, 'b (h c) x y -> b h c (x y)', h=self.heads), qkv)

        q = q.softmax(dim = -2)
        k = k.softmax(dim = -1)

        q = q * self.scale        

        context = torch.einsum('b h d n, b h e n -> b h d e', k, v)

        out = torch.einsum('b h d e, b h d n -> b h e n', context, q)
        out = rearrange(out, 'b h c (x y) -> b (h c) x y', h=self.heads, x=h, y=w)
        return self.to_out(out)