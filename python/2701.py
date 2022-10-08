def funcao(x, n):
    """
    Recebe 2 parametros x (número escolhido) e n (quantidade de vezes que esse número é multiplicado por ele mesmo)
    e retorna a multiplicação desse número x pela a quantidade n
    """
    if n == 0:
        return 1
    else:
        return x * funcao(x, n - 1)
def main():
    x = int(input())    
    n = int(input())
    print(funcao(x, n))
    print(funcao(2, 3))
main()

composer global require laravel/installer
laravel new projeto_ps








controller
<?php

namespace App\Http\Controllers;

use App\Models\Produto;
use App\Models\Categoriadeproduto;
use App\Http\Requests\StoreProdutoRequest;
use App\Http\Requests\UpdateProdutoRequest;
use Illuminate\Support\Facades\Storage;

class ProdutoController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    private $produtos;
    private $categoriadeprodutos;

    public function __construct(Produto $produtos, Categoriadeproduto $categoriadeprodutos)
    {
        $this->produtos = $produtos;
        $this->categoriadeprodutos = $categoriadeprodutos;
    }
    public function index()
    {
        $produtos = $this->produtos->all();
        return view('produto.index', compact('produtos'));
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        $categoriadeprodutos = $this->categoriadeprodutos->all();
        return view('produto.crud', compact('categoriadeprodutos'));
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \App\Http\Requests\StoreProdutoRequest  $request
     * @return \Illuminate\Http\Response
     */
    public function store(StoreProdutoRequest $request)
    {
        $produto = new produto();
        $produto->nome = $request->input('nome');
        $produto->preco = $request->input('preco');
        $produto->descricao = $request->input('descricao');
        $produto->quantidade = $request->input('quantidade');
        $imagem = $request->file('imagem')->store('produtos', 'public');
        $produto->imagem = $imagem;
        $produto->categoriadeprodutos_id = $request->input('categoriadeprodutos_id');
        $produto->save();
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Models\Produto  $produto
     * @return \Illuminate\Http\Response
     */
    public function show(Produto $produto)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Models\Produto  $produto
     * @return \Illuminate\Http\Response
     */
    public function edit(Produto $produto)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \App\Http\Requests\UpdateProdutoRequest  $request
     * @param  \App\Models\Produto  $produto
     * @return \Illuminate\Http\Response
     */
    public function update(UpdateProdutoRequest $request, Produto $id)
    {
        $datas = $request->all();
        $produto = $this->produtos->find($id);

        if ($request->hasFile('imagem')){
            Storage::delete('public/' . $produto->imagem);
            $datas['imagem'] = $request->file('imagem')->store('produtos', 'public');
        }
        $produto->update($datas);
        return redirect('produto');

    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Models\Produto  $produto
     * @return \Illuminate\Http\Response
     */
    public function destroy(Produto $produto)
    {
        //
    }
}
      
model
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Produto extends Model
{
    protected $table = 'produtos';
    protected $fillable = [
        'nome', 'preco', 'descricao', 'quantidade', 'imagem', 'categoriadeproduto_id'];
}
