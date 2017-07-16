#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     14/07/2017
# Copyright:   (c) Ben Cotto 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class NodoPruebas(object):

    def __init__(self, clavesMaximas, leaf):
        assert clavesMaximas >= 3 and clavesMaximas % 2 == 1
        self.clavesMaximas = clavesMaximas
        self.claves = []
        self.hijos = None if leaf else []

    def es_hoja(self):
        return self.hijos is None

    def buscarEnArbolB(self, obj):
        claves = self.claves
        i = 0
        while i < len(claves):
        	if obj == claves[i]:
        		return i
        	elif obj > claves[i]:
        		i += 1
        	else:
        		break
        return ~i

    def eliminar_minimo(self):
        clavesMinimas = len(self.claves) // 2
        node = self
        while not node.es_hoja():
        	assert len(node.claves) > clavesMinimas
        	node = node.verificador_eliminar_hijo(0)
        assert len(node.claves) > clavesMinimas
        return node.eliminar_clave(0)


    def remove_max(self):
        clavesMinimas = len(self.claves) // 2
        node = self
        while not node.es_hoja():
        	assert len(node.claves) > clavesMinimas
        	node = node.verificador_eliminar_hijo(len(node.hijos) - 1)
        assert len(node.claves) > clavesMinimas
        return node.eliminar_clave(len(node.claves) - 1)

    def eliminar_clave(self, index):
        if index < 0 or index >= len(self.claves):
        	raise IndexError()
        return self.claves.pop(index)


    def eliminar_clave_e_hijo(self, keyindex, childindex):
        if keyindex < 0 or keyindex >= len(self.claves):
        	raise IndexError()
        if self.es_hoja():
        	if childindex is not None:
        		raise ValueError()
        else:
        	if childindex < 0 or childindex >= len(self.hijos):
        		raise IndexError()
        	del self.hijos[childindex]
        return self.eliminar_clave(keyindex)

    def dividir(self):
        if len(self.claves) != self.clavesMaximas:
        	raise RuntimeError("no se puede dividir")
        clavesMinimas = self.clavesMaximas // 2
        rightnode = NodoPruebas(self.clavesMaximas, self.es_hoja())
        middlekey = self.claves[clavesMinimas]
        rightnode.claves.extend(self.claves[clavesMinimas + 1 : ])
        del self.claves[clavesMinimas : ]
        if not self.es_hoja():
        	rightnode.hijos.extend(self.hijos[clavesMinimas + 1 : ])
        	del self.hijos[clavesMinimas + 1 : ]
        return (rightnode, middlekey)


    def verificador_eliminar_hijo(self, index):

        assert not self.es_hoja()
        clavesMinimas = self.clavesMaximas // 2
        child = self.hijos[index]
        if len(child.claves) > clavesMinimas:
        	return child
        assert len(child.claves) == clavesMinimas

        ##obtiene hermanos
        left  = self.hijos[index - 1] if index >= 1 else None
        right = self.hijos[index + 1] if index < len(self.claves) else None
        internal = not child.es_hoja()
        assert left is not None or right is not None
        assert left  is None or left .es_hoja() != internal
        assert right is None or right.es_hoja() != internal

        if left is not None and len(left.claves) > clavesMinimas:
        	if internal:
        		child.hijos.insert(0, left.hijos.pop(-1))
        	child.claves.insert(0, self.claves[index - 1])
        	self.claves[index - 1] = left.eliminar_clave(len(left.claves) - 1)
        	return child
        elif right is not None and len(right.claves) > clavesMinimas:
        	if internal:
        		child.hijos.append(right.hijos.pop(0))
        	child.claves.append(self.claves[index])
        	self.claves[index] = right.eliminar_clave(0)
        	return child
        elif left is not None:
        	assert len(left.claves) == clavesMinimas
        	if internal:
        		left.hijos.extend(child.hijos)
        	left.claves.append(self.eliminar_clave_e_hijo(index - 1, index))
        	left.claves.extend(child.claves)
        	return left
        elif right is not None:
        	assert len(right.claves) == clavesMinimas
        	if internal:
        		child.hijos.extend(right.hijos)
        	child.claves.append(self.eliminar_clave_e_hijo(index, index + 1))
        	child.claves.extend(right.claves)
        	return child
        else:
        	raise AssertionError("Impossible condition")

    def check_structure(self, isroot, leafdepth, min, max):

        claves = self.claves
        if not isroot and not (self.clavesMaximas // 2 <= len(claves) <= self.clavesMaximas):
        	raise AssertionError("Invalid number of claves")
        if self.es_hoja() != (leafdepth == 0):
        	raise AssertionError("Incorrect leaf/internal node type")

        tempclaves = [min] + claves + [max]
        for i in range(len(tempclaves) - 1):
        	x = tempclaves[i]
        	y = tempclaves[i + 1]
        	if x is not None and y is not None and y <= x:
        		raise AssertionError("Invalid key ordering")

        # Count keys in this subtree
        count = len(claves)
        if not self.es_hoja():
        	if len(self.hijos) != len(claves) + 1:
        		raise AssertionError("Invalid number of hijos")
        	for (i, child) in enumerate(self.hijos):
        		# Check hijos pointers and recurse
        		if not isinstance(child, NodoPruebas):
        			raise TypeError()
        		count += child.check_structure(False, leafdepth - 1, tempclaves[i], tempclaves[i + 1])
        return count

