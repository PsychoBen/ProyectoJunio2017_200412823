import numbers
import NodoPruebas

class ArbolB(object):

    def __init__(self, grado, coll=None):
        if not isinstance(grado, numbers.Integral):
        	raise TypeError()
        if grado < 2:
        	raise ValueError("Degree must be at least 2")
        self.clavesMinimas = grado - 1
        self.clavesMaximas = grado * 2 - 1

        self.limpiar()
        if coll is not None:
        	for obj in coll:
        		self.insertarNodoArbolB(obj)


    def __len__(self):
        return self.size


    def limpiar(self):
        self.raiz = NodoPruebas.NodoPruebas(self.clavesMaximas, True)
        self.size = 0


    def __contains__(self, obj):
        node = self.raiz
        while True:
        	index = node.buscarEnArbolB(obj)
        	if index >= 0:
        		return True
        	elif node.es_hoja():
        		return False
        	else:  # Internal node
        		node = node.hijos[~index]


    def insertarNodoArbolB(self, obj):
        # Special preprocessing to dividir root node
        raiz = self.raiz
        if len(raiz.claves) == self.clavesMaximas:
        	right, middlekey = raiz.dividir()
        	left = raiz
        	self.raiz = NodoPruebas.NodoPruebas(self.clavesMaximas, False)  # Increment tree height
        	raiz = self.raiz
        	raiz.claves.append(middlekey)
        	raiz.hijos.append(left)
        	raiz.hijos.append(right)

        # Walk down the tree
        node = raiz
        while True:
        	# buscarEnArbolB for index in current node
        	assert len(node.claves) < self.clavesMaximas
        	assert node is raiz or len(node.claves) >= self.clavesMinimas
        	index = node.buscarEnArbolB(obj)
        	if index >= 0:
        		return  # Key already exists in tree
        	index = ~index
        	assert index >= 0

        	if node.es_hoja():  # Simple insertion into leaf
        		node.claves.insert(index, obj)
        		self.size += 1
        		return  # Successfully added
        	else:  # Handle internal node
        		child = node.hijos[index]
        		if len(child.claves) == self.clavesMaximas:  # dividir child node
        			right, middlekey = child.dividir()
        			node.hijos.insert(index + 1, right)
        			node.claves.insert(index, middlekey)
        			if obj == middlekey:
        				return False  # Key already exists in tree
        			elif obj > middlekey:
        				child = right
        		node = child


    def eliminarNodoArbolB(self, obj):
        if not self._eliminarNodoArbolB(obj):
        	raise KeyError(str(obj))

    def discard(self, obj):
        self._eliminarNodoArbolB(obj)


    def _eliminarNodoArbolB(self, obj):
        # Walk down the tree
        raiz = self.raiz
        index = raiz.buscarEnArbolB(obj)
        node = raiz
        while True:
        	assert len(node.claves) <= self.clavesMaximas
        	assert node is raiz or len(node.claves) > self.clavesMinimas
        	if node.es_hoja():
        		if index >= 0:  # Simple removal from leaf
        			node.eliminar_clave(index)
        			self.size -= 1
        			return True
        		else:
        			return False

        	else:  # Internal node
        		if index >= 0:  # Key is stored at current node
        			left, right = node.hijos[index : index + 2]
        			if len(left.claves) > self.clavesMinimas:  # Replace key with predecessor
        				node.claves[index] = left.remove_max()
        				self.size -= 1
        				return True
        			elif len(right.claves) > self.clavesMinimas:
        				node.claves[index] = right.eliminar_minimo()
        				self.size -= 1
        				return True
        			elif len(left.claves) == self.clavesMinimas and len(right.claves) == self.clavesMinimas:
        				# Merge key and right node into left node, then recurse
        				if not left.es_hoja():
        					left.hijos.extend(right.hijos)
        				left.claves.append(node.eliminar_clave_e_hijo(index, index + 1))
        				left.claves.extend(right.claves)
        				if node is raiz and len(raiz.claves) == 0:
        					self.raiz = raiz.hijos[0]  # Decrement tree height
        					raiz = self.raiz
        				node = left
        				index = self.clavesMinimas  # Index known due to merging; no need to buscarEnArbolB
        			else:
        				raise AssertionError("Impossible condition")
        		else:  # Key might be found in some child
        			child = node.verificador_eliminar_hijo(~index)
        			if node is raiz and len(raiz.claves) == 0:
        				self.raiz = raiz.hijos[0]  # Decrement tree height
        				raiz = self.raiz
        			node = child
        			index = node.buscarEnArbolB(obj)


    # Note: Not fail-fast on concurrent modification.
    def __iter__(self):
        if self.size == 0:
        	return

        # Initialization
        nodestack  = []
        indexstack = []
        node = self.raiz
        while True:
        	nodestack.append(node)
        	indexstack.append(0)
        	if node.es_hoja():
        		break
        	node = node.hijos[0]

        # Generate elements
        while len(nodestack) > 0:
        	node = nodestack.pop()
        	index = indexstack.pop()
        	if node.es_hoja():
        		assert index == 0
        		for obj in node.claves:
        			yield obj
        	else:
        		yield node.claves[index]
        		index += 1
        		if index < len(node.claves):
        			nodestack.append(node)
        			indexstack.append(index)
        		node = node.hijos[index]
        		while True:
        			nodestack.append(node)
        			indexstack.append(0)
        			if node.es_hoja():
        				break
        			node = node.hijos[0]


    # For unit tests
    def check_structure(self):
        # Check size and root node properties
        size = self.size
        raiz = self.raiz
        if size < 0 or not isinstance(raiz, ArbolB.Node) or (size > self.clavesMaximas and raiz.es_hoja()) \
        		or (size <= self.clavesMinimas * 2 and (not raiz.es_hoja() or len(raiz.claves) != size)):
        	raise AssertionError("Invalid size or raiz type")

        # Calculate height by descending into one branch
        height = 0
        node = raiz
        while not node.es_hoja():
        	height += 1
        	node = node.hijos[0]

        # Check all nodes and total size
        if raiz.check_structure(True, height, None, None) != size:
        	raise AssertionError("Size mismatch")


    def ObtenerDotArbolB(self):
        dot = "digraph g { node [shape=record];"
        esteNivel = [self.raiz]
        nivel=0
        while esteNivel:
            siguiente_nivel = []
            output = ""
            pagina=0
            for nodo in esteNivel:
                if nodo.hijos:
                    siguiente_nivel.extend(nodo.hijos)
                i = 0
                aux = len(nodo.claves)
                for i in range(0,aux):
                    if(i == 0):
                        output += "Nodo%d_%d[label=\"<P0>" %(nivel, pagina)
                    output = output +"|"+ str(nodo.claves[i]) + "|<P%d>"% (i+1)
                    if(i == aux -1):
                        output += "\"]; "
                pagina += 1
            dot += output
            esteNivel = siguiente_nivel
            nivel += 1

        esteNivel = [self.raiz]
        nivel=0
        while esteNivel:
            siguiente_nivel = []
            output = ""
            pagina=0
            aux2 = 0
            for nodo in esteNivel:
                if nodo.hijos:
                    siguiente_nivel.extend(nodo.hijos)
                i = 0
                aux = len(nodo.hijos)
                for i in range(0,aux):
                    output += "Nodo%d_%d:P%d -> Nodo%d_%d; " %(nivel, pagina, i, nivel+1, aux2)
                    aux2 +=1
                pagina += 1
            dot += output
            esteNivel = siguiente_nivel
            nivel += 1
        dot += "}"
        print(dot)
        return dot